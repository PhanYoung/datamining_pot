# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import sklearn
import numpy as np

def read_id_values(inpath, delimiter='\x01'):
    dat = np.loadtxt(inpath, dtype=str, delimiter=delimiter)
    uid = dat[:, 0]
    value = dat[:, 1:].astype(float)
    return uid, value
    
def read_id_values_mod(inpath, delimiter='\x01'):
    dat = np.loadtxt(inpath, dtype=str, delimiter=delimiter)
    uid = dat[:, 0]
    value = dat[:, 1:-1].astype(float)
    mod = dat[:, -1]
    return uid, value, mod
    
    
    
##readfile
i, v, m = read_id_values('../data/outfile')
##v = sklearn.datasets.make_biclusters((1000, 10), 5)[0]
##v = sklearn.datasets.make_blobs(n_samples=1000, n_features=10, centers=5)[0]
##scaler
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#s = scaler.fit_transform(v)
##denoise
#s[s>3] = 3.
#
##find cluster parameters
#from dmpot.ml.cluster_ import search_k
#best_score = search_k(s, draw=True)
#print best_score
#

#cluster
#n_clusters=20
#from sklearn.cluster import KMeans
#km = KMeans(n_clusters=20)
#r = km.fit_predict(s)
#
#
##stat.
#from collections import Counter
#h = Counter(r)
#
#import matplotlib.pyplot as plt
#from dmpot.draw import split_hist
#seperators = [1, 3, 7, 11, 19, 51]
#for c in xrange(n_clusters):
#    for i in xrange(len(v[0])):
#        print c, i
#        split_hist(v[r==c][:, i], seperators)
#        plt.figure()
#    
    
# TODO: cumulated_grade score distribution

#display
from dmpot.measure_transform import Histogramizer_2D
tags = ["sms", "phone", "game", "photo", "web", "social", "email", "shopping",
        "reading", "video"]
        
h = Histogramizer_2D()
h.fit(v)
u = h.transform(v)
m = np.array([u[r==i].mean(axis=0) for i in range(6)])