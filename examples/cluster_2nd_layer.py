# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

import numpy as np

from dmpot.ml.cluster_ import search_k
from dmpot.draw import draw_radar_set
from dmpot.measure_transform import Histogramizer_2D

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def read_id_values(inpath, delimiter='\x01'):
    dat = np.loadtxt(inpath, dtype=str, delimiter=delimiter)
    uid = dat[:, 0]
    value = dat[:, 1:].astype(float)
    return uid, value
    
def read_id_values_mod(inpath, delimiter='\x01'):
    dat = np.loadtxt(inpath, dtype=str, delimiter=delimiter)
    uid = dat[:, 0]
    value = dat[:, 2:].astype(float)
    mod = dat[:, 1]
    return uid, value, mod


#----------------Config-------------------
_TAGS = ["sms", "phone", "game", "photo", "web", "social", "email", "shopping",
   "reading", "video"]
   
_N_CLUSTERS = 7

_PIC_TITLE = "CLUSTER"

_PIC_PATH = '../data/cluster_result'

_SPACE_RATE = 0.85


if __name__ == "__main__":
    #----------------read data-------------------
    ids, vals = read_id_values()
    
    #----------------scale-------------------
    scaler = StandardScaler()
    s = scaler.fit_transform(vals)
    #denoise
    s[s>3] = 3.
    
    #----------------PCA-------------------
    pca = PCA()
    p_all = pca.fit_transform(s)
    space_ratio = pca.explained_variance_ratio_
    space_sum = 0
    for i, v in enumerate(space_ratio):
        space_sum += v
        if space_sum > _SPACE_RATE:
            break
    n_conponents = i + 1
    p = p_all[:, : n_conponents]
    
    #----------------Cluster-------------------
    n_clusters = search_k(p)
    km = KMeans(n_clusters=n_clusters)
    r = km.fit_predict(p)
    
    #----------------Clusters' Indices-------------------
    hgm = Histogramizer_2D()
    nVal = hgm.fit_transform(vals)
    #indices for all
    all_indices = np.array(nVal.mean(axis=0))
    #indices for each cluster
    clusters_indices = [nVal.mean(axis=0) for i in range(n_clusters)]
    
    #----------------Draw Figures-------------------
    draw_data = [all_indices] + clusters_indices
    titles = ["ALL:%s" % len(nVal)] + ["%s:%s" % ((sum(r==i) * 1. / len(nVal)), 
                                       sum(r==i)) for i in range(_N_CLUSTERS)]
    
    draw_radar_set(draw_data, 2, spoke_labels=_TAGS, pic_title=_PIC_TITLE, 
                   titles=titles, save_path=_PIC_PATH+'.png')

        


    
