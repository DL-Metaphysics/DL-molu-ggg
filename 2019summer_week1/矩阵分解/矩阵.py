import numpy as np 
import matplotlib.pyplot as plt
from math import pow
ls_e=[]#一个列表，把e_2（损失函数）的值放进列表以便画图
def matrix (r,p,q,k,al,ba):
    ls_e=[]
    times=0
    
    while (times<10000):
        times+=1
        for i in range (4):
            for j in range(4):
                if r[i][j]>0:
                    eij=r[i][j]-np.dot(p[i,:],q[:,j])#求损失函数（误差）
                    
                    for k in range(K):
                        
                        pd_p=-2*eij*q[k][j]+ba*p[i][k]
                        pd_q=-2*eij*p[i][k]+ba*q[k][j]
                        p[i][k]=p[i][k]-al*pd_p
                        q[k][j]=q[k][j]-al*pd_q#求偏导更新权值

        e_2=0 ####              
        for i in range (4):
            for j in range(4):
                 if r[i][j]>0:
                     
                    eij=r[i][j]-np.dot(p[i,:],q[:,j])
                    e_2+=eij**2
                    
                    
                    for k in range(K):#大写K，这是你曾经犯下的错误
                        
                        e_2+=(ba/2)*(p[i][k]**2+q[k][j]**2)#e_2表示 eij^2
                        
                        
                        
        ls_e.append(e_2)
                    
    return p,q,ls_e
               

K=3   
al=0.00005
ba=0.05
p=np.random.rand(4,K)
q=np.random.rand(K,4)
r=[[1,3, 0, 4],
[4, 0 ,0 ,7],
[3 ,1, 5, 0],
[2 ,7 ,0 ,5]]
nP,nQ,ls_e=matrix(r,p,q,k,al,ba)
print("原始的评分矩阵R为：\n",r)
R_MF=np.dot(nP,nQ)
print("经过MF算法填充0处评分值后的评分矩阵R_MF为：\n",R_MF)
n=len(ls_e)##也就是循环次数
x=range(n)#画表的用
plt.plot(x,ls_e,color='r',linewidth=3)
plt.title("Convergence curve")
plt.xlabel("generation")
plt.ylabel("loss")
plt.show()
