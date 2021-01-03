# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:17:17 2020

@author: user
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random 

# taille de la matrice
N = 32
# nombre d'iteration de la simulation=intervalFrame
fps = 1#number of actualisation of an image 
nSeconds = 25 #for 25 iterations
nSeconds1= 50 #for 50 iterations
intervalFrame = fps*nSeconds1 #here we have the choice to switch between nSeconds and nSeconds1 

#so by calculating the intervalframe we get between each image one second of sleep you will notice that in
#the video 


#générer una matrice aléatoire
def matricealeatoire():
    
    q=[[random.gauss(0,1) for i in range(32)]for i in range(32)]
    for i in range(len(q)):
        for j in range(len(q[i])):
            if  q[i][j]>0.9:
                 q[i][j]=1
            else:
                 q[i][j]=0
    matrix=np.tile(q,(intervalFrame,1,1))
             
    return matrix
def fichiertxt(ev):
    with open("input1.txt", "w") as f:
        l=[]
        liste=[[0 for i in range(32)]for i in range(32)]
        for i in range(len(ev)):
            for j in range(len(ev[i])):
                m=str(ev[i][j])
                liste[i][j]=m
            P=''.join(liste[i])
            l=l+[P]
        for i in l:
            f.write(i)
            f.write('\n')
    return l      
def create_grille():
    my_file=open("input","r")
    data=my_file.read()
    grille=[] 
    m=data.split("\n")
    for i in range(32):
        liste=[] 
        for j in range(32):
            a=int(m[i][j])
            liste.append(a)   
        grille.append(liste) 
    matrix=np.tile(grille,(intervalFrame,1,1))
    return matrix     
def evol_grille(frame,img):
    global matrix
    grille=matrix[frame].copy()
    for i in range(32):
        for j in range(32):
            if i==0 or j==0 or j==31 or i==31:
                continue
            
            if(grille[i,j]==0):
                if(grille[i+1,j]+grille[i,j+1]+grille[i-1,j]+grille[i,j-1]+grille[i+1,j+1]+grille[i+1,j-1]+grille[i-1,j-1]+grille[i-1,j+1]==3):#Any dead cell with three live neighbours becomes a live cell
                    grille[i,j]=1
            if(grille[i,j]==1):
                if(grille[i+1,j]+grille[i,j+1]+grille[i-1,j]+grille[i,j-1]+grille[i+1,j+1]+grille[i+1,j-1]+grille[i-1,j-1]+grille[i-1,j+1] in [2,3]):#Any live cell with two or three live neighbours survives.
                    grille[i,j]=1
                if(grille[i+1,j]+grille[i,j+1]+grille[i-1,j]+grille[i,j-1]+grille[i+1,j+1]+grille[i+1,j-1]+grille[i-1,j-1]+grille[i-1,j+1]>3)  :#if a living cell is surrounded by more than three living cells, it dies. 
                    grille[i,j]=0
                if(grille[i+1,j]+grille[i,j+1]+grille[i-1,j]+grille[i,j-1]+grille[i+1,j+1]+grille[i+1,j-1]+grille[i-1,j-1]+grille[i-1,j+1]<2) :#if a living cell is surrounded by fewer than two living cells, it dies
                    grille[i,j]=0
    fichiertxt(grille)                   
    matrix[frame+1] = grille.copy()               
    img.set_data(grille)
                  
    return [img]

#main


#animation video gives us the sequence of images between each second
    
get=int(input("if want to use the random matrix choose 1 else choose 2 : "))
if get==1:
    matrix = matricealeatoire()
if get==2:    
    matrix=create_grille()
else:
    get=int(input("please try again a number in[1,2]: "))

        
fig, ax = plt.subplots() 
img = ax.matshow(matrix[0]);
ani = animation.FuncAnimation(fig, evol_grille,fargs=(img,),frames=intervalFrame-2, 
                              interval = 1000/fps,blit=True, repeat=True) 
ani.save(r"input1.mp4", fps=fps, writer='ffmpeg')
plt.show()






