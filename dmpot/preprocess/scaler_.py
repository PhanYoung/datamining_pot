# -*- coding: utf-8 -*-

from sklearn.preprocessing import StandardScaler

def denoise_stand_scale(X, y=None):
    sc = StandardScaler()
    r = sc.fit_transform(X)
    r[r>3] = 3
    
    
def historgramize(X):
    pass


def cumulated_grade(X):
    pass