# -*- coding: utf-8 -*-

from sklearn.cross_validation import cross_val_score

def bias_variance(clf, X, y):
    scores_ = cross_val_score(clf, X, y, cv=5)
    return scores_.mean(), scores_.var(), scores_.min(), scores_