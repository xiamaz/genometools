#ifndef FT_TRIMSTAT_H
#define FT_TRIMSTAT_H
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct GtFtTrimstat GtFtTrimstat;

GtFtTrimstat *gt_ft_trimstat_new(void);

#ifndef NDEBUG
void gt_ft_trimstat_add(GtFtTrimstat *trimstat,
                        bool diedout,
                        GtUword sumvalid,
                        GtUword maxvalid,
                        GtUword d,
                        size_t spaceforfront);
void gt_ft_trimstat_add_matchlength(GtFtTrimstat *trimstat,
                                    uint32_t matchlength);
#else
void gt_ft_trimstat_add(GT_UNUSED GtFtTrimstat *trimstat,
                        GT_UNUSED bool diedout,
                        GT_UNUSED GtUword sumvalid,
                        GT_UNUSED GtUword maxvalid,
                        GT_UNUSED GtUword d,
                        GT_UNUSED size_t spaceforfront);
void gt_ft_trimstat_add_matchlength(GT_UNUSED GtFtTrimstat *trimstat,
                                    GT_UNUSED uint32_t matchlength);
#endif

void gt_ft_trimstat_delete(GtFtTrimstat *trimstat);

void gt_ft_trimstat_out(const GtFtTrimstat *trimstat,bool verbose);

#endif
