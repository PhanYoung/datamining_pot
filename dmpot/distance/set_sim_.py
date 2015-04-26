# -*- coding: utf-8 -*-

def intersect_len(x, y):
    '''计算两个输入集合的交集长度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
                 string需要先转化为unicode
       [Return]
           <int>: 两个集合的交集长度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    ins = x.intersection(y)
    return len(ins)


def cover_sim(x, y):
    '''计算两个输入集合的覆盖率相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的覆盖率相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    return intersect_len(x, y) * 1.0 / min(len(x), len(y)) 


def jaccard(x, y):
    '''计算两个输入集合的Jaccard相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的Jaccard相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    union = x.union(y)
    return intersect_len(x, y) * 1.0 / len(union) 



def dice(x, y):
    '''计算两个输入集合的Dice相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的Dice相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    return intersect_len(x, y) * 2.0 / (len(x) + len(y))
