# -*- coding: utf-8 -*-
import sys
from sklearn.cluster import KMeans
try:
    from ..evaluate import total_compact
except:
    sys.path.append('../evaluate')
    
    
import pylab as pl
import numpy as np

def deriv(Y):
    return [Y[i+1] - Y[i] for i in range(len(Y)-1)]

def search_k_base(X, max_n=20, n_jobs=-1, draw=False):
    scores = []
    for k in range(1, max_n):
        kmod = KMeans(n_clusters=k, n_jobs=n_jobs)
        r = kmod.fit_predict(X)
        score = total_compact(X, r)
        scores.append(score)
        
    D = deriv(scores)
    V = [D[i] / D[i+1] for i in range(len(D)-1)]
    if draw:
        pl.xticks(range(max_n))
        pl.plot(range(1, max_n), scores)
        print D
        print V
    return V.index(max(V)) + 2


def search_k(X, max_n=20, n_jobs=-1, draw=False):
    '''It is sophisticated to set n_clusters as 4 to 16
    '''
    scores = []
    for k in range(1, max_n):
        kmod = KMeans(n_clusters=k, n_jobs=n_jobs)
        r = kmod.fit_predict(X)
        score = total_compact(X, r)
        scores.append(score)
        
    D = deriv(scores)
    V = [D[i] / D[i+1] for i in range(len(D)-1)]
    if draw:
        pl.xticks(range(max_n))
        pl.plot(range(1, max_n), scores)
        print D
        print V
        
    rank_pos = np.argsort(V)[::-1]
    for p in rank_pos:
        if p >= 2 and p <= 14:
            return p+2
    return rank_pos[0] + 2