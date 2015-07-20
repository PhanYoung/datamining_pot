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

def search_k(X, max_n=20, n_jobs=-1, draw=False):
    scores = []
    for k in range(1, max_n):
        kmod = KMeans(n_clusters=k, n_jobs=n_jobs, )
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
