# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cross_validation import train_test_split

def sample(X, y, rate, randseed=49):
    """Sampling input samples 
    Parameters
    ----------
    X<2D-array-like, dtype=float>: features
    y<1D-array-like, dtype=float>: labels
    label<float>: need sampling
    rate<float>: rate < 1, undersampling;
    randseed<int or None>: if randseed < 0, capturing or tiling input sample matrix with axis=0
                           if randseed is None, freely random sampling
    
    Returns
    -------
    <float> correlation coefficient
    """
    if rate >= 1:
        return X, y
    select_X, test_X, select_y, test_y = train_test_split(X, y, 
                                          test_size=int(len(y) * (1-rate)), 
                                          random_state=randseed)
    return select_X, select_y                           



def sample_label(X, y, label, rate, randseed=49):
    """Sampling input samples with denoted label
    Parameters
    ----------
    X<2D-array-like, dtype=float>: features
    y<1D-array-like, dtype=float>: labels
    label<float>: need sampling
    rate<float>: sampling rate. assert(rate > 0),  if rate < 1, undersampling;
                 if rate > 1, oversampling
    randseed<int or None>: if randseed < 0, capturing or tiling input sample matrix with axis=0
                           if randseed is None, freely random sampling
    
    Returns
    -------
    <float> correlation coefficient
    """
    selectX = X[y== label]
    plusCnt = int(len(selectX) * rate)
    if randseed < 0:
        plusIndices = np.array(range(len(selectX)) * int(rate) + 
                               range(plusCnt % len(selectX)))
    else:
        if randseed is not None:
            np.random.seed(randseed)
        plusIndices = np.random.randint(0, len(selectX), plusCnt)
    plusX = selectX[plusIndices]
    plusY = np.tile([label], plusCnt)
    return (np.append(X[y!=label], plusX[plusIndices]).reshape(-1, X.shape[1]), 
            np.append(y[y!=label], plusY)) 