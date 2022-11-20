#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/17


# 计算字符错误率
def cer(r: list, h: list):
    """
    Calculation of CER with Levenshtein distance.
    """

    # initialisation
    import numpy
    d = numpy.zeros((len(r) + 1) * (len(h) + 1), dtype=numpy.uint16)
    d = d.reshape((len(r) + 1, len(h) + 1))
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i


    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(r)][len(h)] / float(len(r))

if __name__ == "__main__":
    r = '从卡耐基'
    h = '从卡耐基'


    print(cer(r, h))



