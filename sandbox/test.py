# -*- coding: utf-8 -*-

from os import sys, path
import numpy as np
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dmpot.preprocess import read_sparse_binary_vector
from dmpot.preprocess import read_sparse_vector
from dmpot.preprocess import sample
from dmpot.ml import BatchClassify

def read_data(filepath):
    lx1 = []
    lx2 = []
    ly = []
    with open(filepath) as f:
        for l in f:
            l = l.strip()
            es = l.split(chr(1))
            lx1.append(read_sparse_binary_vector(eval(es[2]), 1599))
            lx2.append(read_sparse_vector(eval(es[3]), 38)[1:])
            ly.append(int(es[1]))
    return np.array(ly), np.array(lx1), np.array(lx2)
    


def test_effect(X1, y):
    bc = BatchClassify()
    bc.score(X1, y)

    
    
    
#======================#
import dmpot
from dmpot import preprocess
allY, allX1, allX2 = read_data('data.txt')
nx1, ny1 = sample(allX1, allY, 3000)
nx2, ny2 = sample(allX2, allY, 3000)

test_effect(nx1, ny1)

test_effect(nx2, ny2)