# -*- coding: utf-8 -*-
import numpy as np

def general_evaluate(predict_rslt, y):
    '''
    '''
    checkRslt = (predict_rslt, y)
    print "accuracy", sum(checkRslt) * 1. / len(y)
    for i in np.unique(y):
        tp_fn_cnt = sum(y==i)
        tp_fp_cnt = sum(predict_rslt==i)
        tp_cnt = sum((predict_rslt==i)[predict_rslt==y])   
        print i, "precision", tp_cnt * 1. / tp_fp_cnt, \
              "\trecall", tp_cnt * 1. / tp_fn_cnt
              
              
             
    