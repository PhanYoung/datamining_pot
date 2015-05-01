# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
import cPickle as pickle

_VERBOSE = 255

_default_c_range = 2. ** np.arange(-8, 8)
_default_g_range = np.r_[0, 2. **np.arange(-8, 8)]

def reduce_search_range(ori_search_dict, para_dict):
    new_search_dict = {}
    for k in para_dict.keys():
        idx = ori_search_dict[k].index(para_dict[k])
        start, end = max(0, idx - 1), min(idx + 1, len(ori_search_dict[k]) - 1)
        new_search_dict[k] = np.linspace(ori_search_dict[k][start], 
                            ori_search_dict[k][end], 10)
    return new_search_dict


class BaseParamSearcher(object):
    @staticmethod
    def load(self, modelPath):
        return pickle.load(open(modelPath))
    
    def __init__(self):
        self.clf = None
        self.estimator = None
        self.grid = None
        self.done = False

    def train(self, X, y):
        '''
        '''          
        self.grid.fit(X, y)
        self.estimator = self.grid.best_estimator_
        self.done = True
        
    def save(self, recPath):
        pickle.dump(self, open(recPath, 'w'))
        
    def get_model(self, modelPath):
        return self.estimator
                 
    def predict(self, X):
        return self.estimator.predict(X)
        
    def score(self, X, y):
        return self.estimator.score(X, y)



class SvmParamSearcher(BaseParamSearcher):
    def __init__(self, **svm_paras):
        BaseParamSearcher.__init__(self)
        self.clf = svm.SVC(**svm_paras)
        self.grid = GridSearchCV(estimator=self.clf, 
                      param_grid=dict(C=_default_c_range, gamma=_default_g_range),
                      n_jobs=4,
                      cv=5, verbose=_VERBOSE)
        
    def set_search_range(self, c_range=_default_c_range, 
                         g_range=_default_g_range, cv=5, n_jbos=4):
        self.grid.param_grid = dict(C=c_range, gamma=g_range)
        self.n_jobs = n_jbos
        self.cv = cv             
        
    
    
         