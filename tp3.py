# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:20:22 2020

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
import math




 
def randomNumber(d,t):
    l=[]
    for i in range(d,t):
               s=np.random.random()
               l.append(s)
    return l
       
       #task2
def graph(t):
    fig,axs=plt.subplots(3)
    fig.suptitle('Vertically stacked subplots')
    f=randomNumber(0,t)
    axs[0].plot(f)
    axs[1].plot(f[0:t-1],f[1:t],'+')
    plt.hist(f,bins=int(math.sqrt(t)))

    

        
        
#r=randomNumber(0,10)
#print(r)
    


    
    
graph(1000)       

#task3
