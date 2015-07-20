# -*- coding: utf-8 -*-

from collections import Counter
import numpy as np

def cumulated_grade(X):
    cnt = Counter(X)




class CumulatedGrader(object):
    def __init__(self, n_grades=10):
        self.n_grades = n_grades
        self.seperators_ = []
    
    def _sep(self, x_sorted, n_grades):
        if len(x_sorted) and n_grades > 1:
            pos = (len(x_sorted) + n_grades - 1.) / n_grades 
            self.seperators_.append(x_sorted[pos])
            self._sep(x_sorted[x_sorted > x_sorted[pos]], n_grades-1)
        
    
    def fit(self, X):
        self.seperators_=[]
        x_sorted = np.array(sorted(X))
        self._sep(x_sorted, self.n_grades)
        
        
    def predict_one(self, x):
        if x <= 0 :
            return 0
        for i, sep in enumerate(self.seperators_):
            if sep >= x:
                return i + 1
        return i + 2
        
            
    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])

    def transform(self, X):
        return self.predict(X)


class Histogramizer(object):
    def __init__(self):
        self.hist_x_ = None
        self.hist_y_ = None
        self.total_ = 0
        
    def fit(self, X):
        self.hist_ = Counter(X)
        self.hist_x_ = np.array(sorted(self.hist_.keys()))
        self.hist_y_ = np.array([self.hist_[x] for x in self.hist_x_])
        self.hist_acc_ = [sum(self.hist_y_[:i]) for i in range(len(self.hist_x_))]
        self.total_ = self.hist_acc_[-1]

    def transform_one(self, x):
        if x < self.hist_x_[0]:
            return 0.
            
        if x > self.hist_x_[-1]:
            return 1.
            
        return sum(self.hist_y_[self.hist_x_ < x]) * 1. / self.total_ 
        #TO IMPROVE
        
    def transform(self, X):
        return np.array([self.transform_one(x) for x in X])
    