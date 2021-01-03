# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:50:29 2020

@author: user
"""
import numpy as np
import Levenshtein as lv
import itertools


def hamming(str1,str2):
    d=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            d=d+1
    return d        

#a='ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC'
#b='GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA'
#print(hamming(a,b))

def levenshtein(s1,s2):
    m=len(s1);n=len(s2)
    d1=np.zeros((m+1,n+1))
    for i in range(1,m+1):
        d1[i,0]=i
    for j in range(1,n+1):
        d1[0,j]=j
    for j in range(1,n+1):
        for i in range(1,m+1):
            insertcost=d1[i-1,j]+1
            deletecost=d1[i,j-1]+1
            if s1[i-1]==s2[j-1]:
                subcost=d1[i-1,j-1]
            else:    
                subcost=d1[i-1,j-1]+1
            d1[i,j]=min(insertcost,deletecost,subcost)
    return d1[m,n],d1


print(lv.distance('python','kryptonite'))
print(levenshtein('python','kryptonite'))



def the_score_matrix(a, b, match_score=3, gap_cost=2):
    H = np.zeros((len(a) + 1, len(b) + 1), np.int)

    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        match = H[i - 1, j - 1] + (match_score if a[i - 1] == b[j - 1] else - match_score)
        delete = H[i - 1, j] - gap_cost
        insert = H[i, j - 1] - gap_cost
        H[i, j] = max(match, delete, insert, 0)
    return H
#H=the_score_matrix(a,b)
#print(H)
def traceback(H, b, b_='', old_i=0):
    # flip H to get index of **last** occurrence of H.max() with np.argmax()
    H_flip = np.flip(np.flip(H, 0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  # (i, j) are **last** indexes of H.max()
    if H[i, j] == 0:
        return b_, j
    b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_
    return traceback(H[0:i, 0:j], b, b_, i)

def smith_waterman(a, b, match_score=3, gap_cost=2):
    a, b = a.upper(), b.upper()
    H = the_score_matrix(a, b, match_score, gap_cost)
    b_, pos = traceback(H, b)
    return pos, pos + len(b_)

#main
str1=input('enter the first DNA sequence: ')
str2=input('enter the second DNA sequence: ')
#a, b = 'GGTTGACTA', 'TGTTACGG'
H = the_score_matrix(str1, str2)
print(H)
print(traceback(H, str2)) # ('gtt-ac', 1)

#a, b = 'GGTTGACTA', 'TGTTACGG'
start, end = smith_waterman(str1, str2)
print(str1[start:end])     # GTTGAC 

        