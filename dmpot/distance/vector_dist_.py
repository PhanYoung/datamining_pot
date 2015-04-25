# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
from scipy.stats.stats import pearsonr

def cosine(x, y):
    """Cosine
    Parameters
    ----------
    x, y : array-like, dtype=float
    
    Returns
    -------
    float
    """
    return np.dot(x, y) / np.linalg.norm(x) / np.linalg.norm(y)
    
    
def pearson(x, y):
    """Calculates a Pearson correlation coefficient
    Parameters
    ----------
    x<array-like, dtype=float>, y<array-like, dtype=float>
    
    Returns
    -------
    <float> correlation coefficient
    """
    #return np.corrcoef(x, y)[0][1]
    return pearsonr(x, y)[0]