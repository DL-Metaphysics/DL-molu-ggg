
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:23:32 2019

@author: 陌路放歌
"""

import numpy as np 
import matplotlib.pyplot as plt

import math
x=np.array([0.05,0.10])#数值
w=np.array([[0.15,0.25],[0.2,0.3]])#权重
ww=np.array([[0.4,0.5],[0.45,0.55]])#第二层权重
o=[0.01,0.99]
ls=[]
times=0
b=0.5
al=0.05
pd_net=[0,0]
net=[[0,0],[0,0]]
out=[[0,0],[0,0]]

while(times<10000):
    times+=1
    net[0]=np.dot(x,w)+b
    net[1]=np.dot(x,ww)+b



    for i in range(2):
        out[0][i]=1/(1+math.exp(-net[0][i]))
        out[1][i]=1/(1+math.exp(-net[1][i]))#正向计算加权求和
        
    
    
    
    
    #对w5-w8求导：
    for i in range(2):#权值第二层的x坐标
        for j in range(2):#权值第二层的y坐标
            
            pd_net[j]=-(o[j]-out[1][j])*out[1][j]*(1-out[1][j])
            pd_w= pd_net[j]*out[0][j]
            ww[i][j]=ww[i][j]-al*pd_w  #第二层所有权重的更新
            
    #对w1-w4求导并更新：
        for i in range(2):
            pd_w1=(pd_net[0]*ww[0][0]+pd_net[1]*ww[0][1])*out[i][0]*x[i]
            pd_w2=(pd_net[0]*ww[1][0]+pd_net[1]*ww[1][1])*out[i][0]*x[i]
            w[i][0]-=al*pd_w1
            w[i][1]-=al*pd_w2
    E=1/2*((o[0]-out[1][0])**2+(o[1]-out[1][1]) **2)
    ls.append(E)
   
            
print(w)
print(ww)
time=range(10000)
plt.plot(time,ls)
plt.show()
