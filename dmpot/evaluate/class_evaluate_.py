# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import figure
def general_evaluate(predict_rslt, y):
    '''
    '''
    checkRslt = (predict_rslt==y)
    print "accuracy", sum(checkRslt) * 1. / len(y)
    for i in np.unique(y):
        tp_fn_cnt = sum(y==i)
        tp_fp_cnt = sum(predict_rslt==i)
        tp_cnt = sum((predict_rslt==i)[predict_rslt==y])   
        print i, "precision", tp_cnt * 1. / tp_fp_cnt, \
              "\trecall", tp_cnt * 1. / tp_fn_cnt
              




            
             
def auc(predict_rslt, y, pos_val=1, step=0.01, 
        f_func=lambda x, y: 2.*x*y/(x+y), draw=False):
    plist = []
    rlist = []
    flist = []
    for i in np.arange(0, 1, step):
        tp_cnt = sum(y[predict_rslt>i] == 1) * 1.
        precision = tp_cnt / sum(predict_rslt>i)
        recall = tp_cnt / sum(y==1)
        plist.append(precision)
        rlist.append(recall)
        flist.append(f_func(precision, recall))
        
    plot(rlist, plist)
    figure()
    plot(np.arange(0, 1, step), flist)
    plot(np.arange(0, 1, step), rlist)
    plot(np.arange(0, 1, step), plist)
    return np.array(flist), np.array(plist), np.array(rlist)
    
    
def classify_threshold(predict_rslt, y, step=0.01, 
                       min_precision=0.8):
    for i in np.arange(0, 1, step):
        tp_cnt = sum(y[predict_rslt>i] == 1) * 1.
        precision = tp_cnt / sum(predict_rslt>i)
        recall = tp_cnt / sum(y==1)
    return np.arange(0, 1, step), np.array(flist)