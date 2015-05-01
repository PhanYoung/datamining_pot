# -*- coding: utf-8 -*-

import numpy as np

def read_sparse_binary_vector(idices, ftr_size=1000):
    ftr_vec = np.zeros(ftr_size)
    ftr_vec[idices] = 1
    return ftr_vec
    
    
def read_sparse_vector(value_dict, ftr_size=1000):
    ftr_vec = np.zeros(ftr_size)
    ftr_vec[value_dict.keys()] = value_dict.values()
    return ftr_vec
    
    
