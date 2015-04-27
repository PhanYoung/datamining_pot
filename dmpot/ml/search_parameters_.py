# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
import cPickle as pickle

_VERBOSE = True

_default_range = [0]


def reduct_search_range(ori_search_dict, para_dict):
    new_search_dict = {}
    for k in cur_dict.keys():
        idx = ori_search_dict[k].index(para_dict[k])
        start, end = max(0, idx - 1), min(idx + 1, len(ori_search_dict[k]) - 1)
        new_search_dict[k] = range(ori_search_dict[k][start], 
                            ori_search_dict[k][end])
    return new_search_dict

class ParamSearcher(object):
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
        self.estimator = self.grid_.best_estimator_
        self.done = True
        
    def save_training_process(self, recPath):
        pickle.dump(self, open(recPath, 'w'))
        
    def get_model(self, modelPath):
        return self.estimator_
                 
    def predict(self, X):
        return self._estimator.predict(X)
        
    def score(self, X, y):
        return self.estimator_.score(X, y)



class SvmParamSearcher(ParamSearcher):
    def __init__(self, **svm_paras):
        ParamSearcher.__init__(self)
        self.clf = svm.SVC(**svm_paras)
        
    def set_search_range(self, c_range=_default_range, 
                         g_range=_defaut_range, n_folds=5):
        self.grid = GridSearchCV(estimator=self.clf, 
                                  param_grid=dict(C=c_range, gamma=g_range),
                                  n_jobs=10,
                                  cv=n_folds, verbose=_VERBOSE)
        
    
    
         