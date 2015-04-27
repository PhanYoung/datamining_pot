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
    
    
def euclid(x, y):
    """Euclidean distance
    """
    return np.linalg.norm(np.array(x) - np.array(y))
    
    
def pair_dist(X):
    gridx, gridy = np.indices([len(X), len(X)])
    grid = np.c_[gridx.ravel(), gridy.ravel()]
    return grid, [euclid(X[i], X[j]) for i, j in grid]