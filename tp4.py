# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:17:15 2020

@author: user

"""
import time 
import math
import numpy as np
import matplotlib . pyplot as plt
def bubblesort(badList):
    i=1
    n=len(badList)-1
    while i<=n:
        j=i
        while j>0 and badList[j-1]>badList[j]:
            badList[j],badList[j-1]=badList[j-1],badList[j]
            j=j-1
        i=i+1
    return badList    
def siftdown(liste,s,e):
    root=s
    while 2*root<=e:
        child=2*root
        sw=root
        if liste[sw-1]<liste[child-1]:
            sw=child
        if child+1<=e and liste[sw-1]<liste[child] :
            sw=child+1
        if sw==root:
            return liste
        else:
            liste[root-1],liste[sw-1]=liste[sw-1],liste[root-1]
            root=sw
    return liste
def heapify(liste,end):
    start=math.floor(end/2)
    while start>=1:
        l=siftdown(liste,start,end)
        start=start-1
    return l
def heapsort(liste):
    liste=heapify(liste,len(liste))
    end=len(liste)
    while end>1:
        liste[end-1],liste[0]=liste[0],liste[end-1]
        end=end-1
        liste=siftdown(liste,1,end)
    return liste
#this function tells which of the two methods is faster 
def time_comparison(l):
    a=time.perf_counter()
    bubblesort(l)
    time1=time.perf_counter() - a
    
    
    b=time.perf_counter()
    heapsort(l)
    time2=time.perf_counter() - b
    
    if time1>time2:
        print('heapsort is faster')
    else:
        print('bubblesort is faster')
    return time1,time2    












#remarque:ces algorithmes renvoient les indices des élément cherché dans la liste 
def sequencial_search(l,a):
    for i in l:
        if i==a:
            return l.index(i)
    else:        
        return None
def dichotomic_search(liste,valrech):
    d=1
    f=len(liste)
    while d<=f:
        m=int((d+f)/2)
        if liste[m]==valrech:
            return m
        elif liste[m]<valrech:
            d=m+1
            if liste[d]==valrech:
                return d
        else:
            f=m-1
            if liste[f]==valrech:
                return f
    return -1          
#this function tells which of the two methods is faster    
def time_comparison2(l,x):
    a=time.perf_counter()
    sequencial_search(l,x)
    time1=time.perf_counter() - a
    
    
    b=time.perf_counter()
    dichotomic_search(l,x)
    time2=time.perf_counter() - b
    
    if time1>time2:
        print('dichotomic search is more efficient ')
    else:
        print('sequencial search is more efficient')
    return time1,time2  








#main code1:this main code is showing each time for a random input array which method is faster
#in level of sorting 
    
#1)heapsort is more efficient than bubblesort because there is the functions inside function 
l=[];l1=[];l2=[]
for i in range(3,13):
    liste=np.random.randint(15,size=2**i)
    time1,time2=time_comparison(liste)
    j=len(liste)
    l.append(j)
    l1.append(time1)
    l2.append(time2)
plt.plot(l,l1,"blue",label="bubble sort")
plt.plot(l,l2,"red",label="heapsort")
plt.legend(loc="upper left")
plt.show()#on the graphics it is clear as the sun light that heapsort is faster 
#2)on small classic arrays the bubblesort is faster than heapsort but when it comes to testing huge random
#inputs the faster algorithm is the heapsort





#main code:2
l=[];l1=[];l2=[]
for i in range(3,13):
    liste=sorted(np.random.randint(20,size=2**i))#we sort the list because of the dichotomic search
    time1,time2=time_comparison2(liste,liste[6])
    j=len(liste)
    l.append(j)
    l1.append(time1)
    l2.append(time2)
plt.plot(l,l1,"blue",label='sequencial search')
plt.plot(l,l2,"red",label='dichotomic search')
plt.legend(loc="upper left")
plt.show()#on the graphics the sequencial search is faster on most cases( sometimes we notice that dicho
#is faster but it happen rarely that why we dont take consideration of it  ) 
#we can see that dichotomic search is slower than sequencial search 








 







        
    
    