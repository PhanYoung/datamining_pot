# -*- coding: utf-8 -*-
import numpy as np

def editdist(s1, s2):
    '''Calculating the edit-distance of *s1* and *s2*
       Parameters
       ----------
       s1/s2 <sequense_like>: input sequenses
       
       Return
       ----------
       <int>: edit-distance of *s1* and *s2*
    '''
    len1 = len(s1)
    len2 = len(s2)
    #recMatrix用来存放已经解过的子问题
    recMatrix = np.zeros((len1+1, len2+1), dtype=int)

    #记录边界条件
    recMatrix[:, 0] = range(len1+1)
    recMatrix[0, :] = range(len2+1)

    for m in xrange(len1):
        for n in xrange(len2):
            #cmpList用来存放候选的子问题推导式
            cmpList = [recMatrix[m, n+1] + 1, recMatrix[m+1, n] + 1]
            if m >= 1 and n >= 1 and s1[m-1] == s2[n] and s1[m] == s2[n-1] :
                cmpList.append(recMatrix[m-1, n-1] + 1)
            if s1[m] == s2[n]:
                cmpList.append(recMatrix[m, n])
            else:
                cmpList.append(recMatrix[m, n]+1)
            #从候选集中选出最优值
            recMatrix[m+1, n+1] = min(cmpList)
    return recMatrix[len1, len2]


def norm_editdist(s1, s2):
    '''返回标准化的编辑距离
    '''
    return editdist(s1, s2) * 1.0 / max(len(s1), len(s2))


def lcs(s1, s2, get_seq=True):
    '''Calculating the longest-common-sequense of *s1* and *s2*
       Parameters
       ----------
       s1/s2 <sequense_like>: input sequenses
       
       Return
       ----------
       <int>: length of longest-common-sequense of *s1* and *s2*
       <list>: longest-common-sequense of *s1* and *s2*
    '''
    len1 = len(s1)
    len2 = len(s2)
    recMatrix = np.zeros((len1+1, len2+1), dtype=int)
    directMatrix = np.zeros((len1+1, len2+1), dtype=int)
    # 1, left; 2, up; 3, left-up
    for m in xrange(len1):
        for n in xrange(len2):
            if s1[m] == s2[n]:
                recMatrix[m+1, n+1] = recMatrix[m, n] + 1
                directMatrix[m+1, n+1] = 3
            else:
                if recMatrix[m, n+1] > recMatrix[m+1, n]:
                    recMatrix[m+1, n+1] = recMatrix[m, n+1]
                    directMatrix[m+1, n+1] = 2
                else:
                    recMatrix[m+1, n+1] = recMatrix[m+1, n]
                    directMatrix[m+1, n+1] = 1
                    
    lcsLen = recMatrix[len1, len2]
    if not get_seq:
        return lcsLen, None
    idx1, idx2 = len1, len2
    retSeq = [''] * lcsLen
    i = lcsLen - 1
    while i >= 0 and idx1 >= 0 and idx2 >= 0:
        if directMatrix[idx1, idx2] == 3:
            retSeq[i] = s1[idx1-1]
            idx1 -= 1
            idx2 -= 1
            i -= 1
        elif directMatrix[idx1, idx2] == 2:
            idx1 -= 1
        else:
            idx2 -= 1
    return lcsLen, retSeq


def lcs_sim(s1, s2, sim_type='dice'):
    '''Calculating similiarity vai lcs
    [Parameters]
        s1/s2 <sequense_like>： input sequenses
        sim_type <str>: ['dice', 'jaccard', 'cover']

    [Return]
       <float>: LCS相似度
    '''
    lcsLen = lcs(s1, s2, False)[0]
    if not lcsLen:
        return 0
    len1, len2 = len(s1), len(s2)
    if sim_type == 'dice':
        scaleSize = (len1 + len2) / 2.
    elif sim_type == 'jaccard':
        scaleSize = len1 + len2 - lcsLen
    else:
        scaleSize = min(len(s1), len(s2))
    return lcsLen * 1.0 / scaleSize
