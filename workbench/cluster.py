# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import sklearn
import numpy as np
from dmpot.ml.cluster_ import search_k
from sklearn.cluster import KMeans
from dmpot.draw import draw_radar_set
from dmpot.measure_transform import Histogramizer_2D

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
    
    
draw_data = []

#分统一标尺和非统一
#hgm = Histogramizer_2D()
#hgm.fit(val)
#nVal = hgm.transform(val)
#vMean = np.array(nVal.mean(axis=0))
draw_data.append(vMean)

    
##v = sklearn.datasets.make_biclusters((1000, 10), 5)[0]
##v = sklearn.datasets.make_blobs(n_samples=1000, n_features=10, centers=5)[0]
    
#readfile
#print "reading..."
#imei, val, mod = read_id_values_mod('../data/user_info_with_model.lst')
#modlist = ['K50-T5', 'Z90-7']
#modlist = list(set(mod))
    
    
#cluster FOR ALL
    
    
    
    
#v = val
    
    
    
    
    
    
    
#hgm = Histogramizer_2D()
#hgm.fit(v)
#nVal = hgm.transform(v)
#vMean = np.array(nVal.mean(axis=0))
#draw_data.append(vMean)

##scaler
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#s = scaler.fit_transform(v)
##denoise
#s[s>3] = 3.

#print 'clustering...'
n_clusters = 7
#km = KMeans(n_clusters=n_clusters)
#r = km.fit_predict(s)



means = [nVal.mean(axis=0) for i in range(n_clusters)]
draw_data += means

tags = ["sms", "phone", "game", "photo", "web", "social", "email", "shopping",
   "reading", "video"]
titles = ["ALL:%s" % len(nVal)] + ["%s:%s" % ((sum(r==i) * 1. / len(nVal)), sum(r==i)) for i in range(n_clusters)]
draw_radar_set(draw_data, 2, spoke_labels=tags, pic_title=m, titles=titles, save_path='../data/'+m+'.png')


#output result
#rslt = np.vstack((imei, r)).T
#np.savetxt('../data/all_cluster_rslt', rslt, delimiter='\t', fmt='%s')



#for m in modlist:
#    try:
#        v = val[mod == m]
#        if len(v) < 1000:
#            continue
#        
#        print 'histograming...'
#        draw_data = []
#        hgm = Histogramizer_2D()
#        hgm.fit(v)
#        nVal = hgm.transform(v)
#        vMean = np.array(nVal.mean(axis=0))
#        draw_data.append(vMean)
#        
#        ##scaler
#        from sklearn.preprocessing import StandardScaler
#        scaler = StandardScaler()
#        s = scaler.fit_transform(v)
#        #denoise
#        s[s>3] = 3.
#        
#        print 'clustering...'
#        n_clusters = 7
#        km = KMeans(n_clusters=n_clusters)
#        r = km.fit_predict(s)
#        
#        means = [nVal[r==i].mean(axis=0) for i in range(n_clusters)]
#        draw_data += means
#        
#        tags = ["sms", "phone", "game", "photo", "web", "social", "email", "shopping",
#           "reading", "video"]
#        titles = ["ALL:%s" % len(nVal)] + ["%s:%s" % ((sum(r==i) * 1. / len(nVal)), sum(r==i)) for i in range(n_clusters)]
#        draw_radar_set(draw_data, 2, spoke_labels=tags, pic_title=m, titles=titles, save_path='../data/'+m+'.png')
#    except:
#        continue

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
#from dmpot.measure_transform import Histogramizer_2D
#tags = ["sms", "phone", "game", "photo", "web", "social", "email", "shopping",
#        "reading", "video"]
#        
#h = Histogramizer_2D()
#h.fit(v)
#u = h.transform(v)
#m = np.array([u[r==i].mean(axis=0) for i in range(6)])