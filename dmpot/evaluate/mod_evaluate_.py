# -*- coding: utf-8 -*-

from sklearn.cross_validation import cross_val_score

def bias_variance(clf, X, y, interept=False):
    scores_ = cross_val_score(clf, X, y, cv=5)
    if interept:
        return "mean:%s, var:%s, min:%s, score:%s)" % (scores_.mean(), scores_.var(), scores_.min(), scores_)
    else:
        return scores_.mean(), scores_.var(), scores_.min(), scores_