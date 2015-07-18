# -*- coding: utf-8 -*-
import numpy as np
from ..distance import euclid
def compactness(X):
    '''内聚度
    '''
    return np.var(X, axis=0).sum()
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