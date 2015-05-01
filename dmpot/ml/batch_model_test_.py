# -*- coding: utf-8 -*-
from ..evaluate import bias_variance
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression


class BatchClassify(object):
    
    def __init__(self):
        self.svc = SVC()
        self.gbdt = GradientBoostingClassifier()
        self.nb = GaussianNB()
        self.lr = LogisticRegression()
        
        
    def fit(self, X, y):
        self.svc.fit(X, y)
        self.gbdt.fit(X, y)
        self.nb.fit(X, y)
        self.lr.fit(X, y)
        
    
    def score(self, X, y):
#        score_list = [  ("svc", self.svc.score(X, y)),
#                        ("gbdt", self.gbdt.score(X, y)),
#                        ("nb", self.nb.score(X, y)),
#                        ("lr", self.lr.score(X, y))  ]
        score_list = [ ("svc", bias_variance(self.svc, X, y)),
                        ("gbdt", bias_variance(self.gbdt, X, y)),
                        ("nb", bias_variance(self.nb, X, y)),
                        ("lr", bias_variance(self.lr, X, y)) ]
        print "\n".join(["%s:%s" % (i[0], i[1]) for i in score_list])
        return score_list

    
