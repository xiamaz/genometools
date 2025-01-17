#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Daniel Standage <daniel.standage@gmail.com>
# Copyright (c) 2009 Brent Pedersen <bpederse@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

from gt.bytes import gtbytes
from gt.dlload import gtlib
from gt.extended.genome_stream import GenomeStream


class DuplicateFeatureStream(GenomeStream):

    def __init__(self, genome_stream, dest_type, source_type):
        self.gs = gtlib.gt_dup_feature_stream_new(genome_stream._as_parameter_,
                                                  gtbytes(dest_type),
                                                  gtbytes(source_type))
        self._as_parameter_ = self.gs

    def from_param(cls, obj):
        if not isinstance(obj, DuplicateFeatureStream):
            raise TypeError("argument must be a DuplicateFeatureStream")
        return obj._as_parameter_

    from_param = classmethod(from_param)

    def register(cls, gtlib):
        from ctypes import c_void_p, c_char_p
        gtlib.gt_dup_feature_stream_new.restype = c_void_p
        gtlib.gt_dup_feature_stream_new.argtypes = [c_void_p, c_char_p,
                                                    c_char_p]

    register = classmethod(register)
