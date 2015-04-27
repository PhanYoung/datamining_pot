# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot


def bins_hist(x, bins):
    """Compute and draw the histogram of *x* with given bins
    Parameters
    ----------
    x <array_like> : input values
    bins <array_like> : edges of bins, len(bins) == n_bins + 1
    """
    histStat = np.histogram(x, bins)
    cnts = histStat[0]
    labels = ["%s-%s"%(bins[i], bins[i+1]) for i in range(len(bins)-1)]
    pyplot.xticks(range(len(cnts)), labels)
    return pyplot.bar(range(len(histStat[0])), cnts, align='center')
    
    
def split_hist(x, seps):
    """Compute and draw the histogram of *x* with given seperators
    Parameters
    ----------
    x <array_like> : input values
    seps <array_like> : seperators of bins, len(seps) == n_bins - 1
    """
    bins = [x.min()] + list(seps) + [x.max()]
    return bins_hist(x, bins)
    

from ..stat import count_all    
def desc_distribute(x, log=False):
    cnts = count_all(x).values()
    if log:
        cnts = np.log(cnts)
    pyplot.plot(sorted(cnts, reverse=True))
    