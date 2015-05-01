# -*- coding: utf-8 -*-

from os import sys, path
import numpy as np
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dmpot.preprocess import read_sparse_binary_vector
from dmpot.preprocess import read_sparse_vector

def read_data(filepath):
    lx1 = []
    lx2 = []
    ly = []
    with open(filepath) as f:
        for l in f:
            l = l.strip()
            es = l.split(chr(1))
            lx1.append(read_sparse_binary_vector(eval(es[2]), 1599))
            lx2.append(read_sparse_vector(eval(es[3]), 38))
            ly.append(int(es[1]))
    return np.array(ly), np.array(lx1), np.array(lx2)