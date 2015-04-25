# -*- coding: utf-8 -*-

from sklearn.svm import SVC
SVM = SVC
from sklearn.svm import SVR

from sklearn.ensemble import GradientBoostingClassifier
GBDT = GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
GBRT = GradientBoostingRegressor

__all__ = ['SVM', 
           'SVR',
           'GBDT',
           'GBRT'
           ]