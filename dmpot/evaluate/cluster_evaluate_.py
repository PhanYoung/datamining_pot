# -*- coding: utf-8 -*-
import numpy as np
from ..distance import euclid

def cluster_center_compact(X, c):
    '''到中心的distance
    '''
    #return reduce(lambda a,b: a+b, map(lambda x: np.linalg.norm(x-c), X))
    return sum([np.linalg.norm(x-c) for x in X])
    
def total_center_compact(X, tag, c):
    return sum([cluster_center_compact(X[tag==t], c[t]) for t in set(tag)])

def cluster_compact(X):
    '''内聚度
    '''
    return np.var(X, axis=0).sum()
    #等价于下面的
    #c = X.mean(axis=0)
    #return np.mean([np.linalg.norm(c-x, 2) ** 2 for x in X])
    
def total_compact(X, tag, verbose=False):
    '''内聚度
    '''
    if verbose:
        print [sum(tag == t) for t in set(tag)]
        print [cluster_compact(X[tag == t]) for t in set(tag)]
    return sum([cluster_compact(X[tag == t]) * sum(tag == t) for t in set(tag)]) * 1. / len(X)
    #等价于下面的
    #c = X.mean(axis=0)
    #return np.mean([np.linalg.norm(c-x, 2) ** 2 for x in X])


def r_square(Xs):
    '''簇差
    Xs <3D-array_like>: clusters - samples - features
    '''
    pass


def rmsstd(Xs):
    pass


def cluster_diff(Xs):
    '''
    '''
    centers = [np.mean(X, axis=0) for X in Xs]
    xx, yy = np.mgrid[0:5, 0:4]
    gridx, gridy = np.indices([len(Xs), 2])
    grid = np.c_[gridx.ravel(), gridy.ravel()]
    return sum([euclid(centers[i[0]], centers[i[1]]) for i in grid])