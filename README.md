# 推导作业如下
[image](https://github.com/DL-Metaphysics/DL-molu-ggg/blob/master/1.png)
[image](https://github.com/DL-Metaphysics/DL-molu-ggg/blob/master/2.png)
[image](https://github.com/DL-Metaphysics/DL-molu-ggg/blob/master/3.png)


# 房屋价格与面积关系题
import numpy as np
import matplotlib.pyplot as plt 

x=[150,200,250,300,350,400,600]
y=[6450,7450,8450,9450,11450,15450,18450]#x,y两组数据
theta0,theta1=0,0#theta就是所求两个参数
al=0.000001#al就是alpha，学习效率
m=len(x)#样本总数
max=1000000#最大循环次数
print("请等待大概30s，若不想等待，请修改max值")
def piliang (x,y,theta0,theta1,al,m,max):
    
    for j in range (max):
        m1,m2=0,0
        sum1,sum2=0,0
        error=0
        k=0.000000001
        
        
         
        for i in range(m):
            dianta=theta0+theta1*x[i]-y[i]
            m1+=dianta
            m2+=(dianta)*x[i]
            
            sum1+=m1      #批量函数，计算  ∑（h[i]-y[i]) i 从1 到 m
            sum2+=m2
        theta0-=(al/m)*sum1
        theta1-=(al/m)*sum2
        for t in range(m):
            error+=(theta0+theta1*x[t]-y[t])**2   #计算误差
        if error<k:#判断是否误差可以允许的范围
            break
        
    return theta0,theta1

def suiji (x,y,theta0,theta1,al,m,max):
    error=0
    k=0.0000001
    for j in range (max):
        m1,m2=0,0#
        for i in range(m):
            m1+=theta0+theta1*x[i]-y[i]  #计算h[i]-y[i]
            m2+=(theta1*x[i]-y[i])*x[i]
       
            theta0-=(al/m)*m1   #迭代更新,不断更新迭代知道迭代次数达到最大值或满足条件
            theta1-=(al/m)*m2
            
       
            
           
        for t in range(m):
            error+=(theta0+theta1*x[t]-y[t])**2  #计算误差
        if error<k:#判断是否误差可以允许的范围
            break
            
    return theta0,theta1


theta0,theta1= piliang (x,y,theta0,theta1,al,m,max)
theta2,theta3= suiji (x,y,theta0,theta1,al,m,max)
print("(批量梯度值) :{} {}". format(theta0,theta1))
print("（随机梯度）:{} {}". format(theta2,theta3))
#以下是画图代码，可忽略


print("继续等待散点图以及拟合的线性函数")
plt.scatter(x,y)
xx=np.linspace(0,12,30)


plt.title("the contact betwee YearsExperience and  salary")
plt.xlabel(" YearsExperience")
plt.ylabel("salary")
h1=theta1*xx+theta0
h2=theta3*xx+theta2
plt.plot(xx,h1,"r--",label="red:batch-green:random")
plt.plot(xx,h2,"g^")
plt.show()
print("红虚线代表批量梯度所得，绿三角石随机梯度所得")



#所得到的对比图像是：
[image](https://github.com/DL-Metaphysics/DL-molu-ggg/blob/master/%E5%B7%A5%E8%B5%84.png)

#工资与阅历关系
import numpy as np
import matplotlib.pyplot as plt 
x=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
y=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,
   55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
#x,y两组数据
theta0,theta1=0,0#theta就是所求两个参数
al=0.000001#al就是alpha，学习效率
m=len(x)#样本总数
max=1000000#最大循环次数
print("请等待大概30s，若不想等待，请修改max值")
def piliang (x,y,theta0,theta1,al,m,max):
    
    for j in range (max):
        m1,m2=0,0
        sum1,sum2=0,0
        error=0
        k=0.000000001
        
        
         
        for i in range(m):
            dianta=theta0+theta1*x[i]-y[i]
            m1+=dianta
            m2+=(dianta)*x[i]
            
            sum1+=m1#批量函数，计算  ∑（h[i]-y[i]) i 从1 到 m
            sum2+=m2
        theta0-=(al/m)*sum1
        theta1-=(al/m)*sum2
        for t in range(m):
            error+=(theta0+theta1*x[t]-y[t])**2#计算误差
        if error<k:#判断是否误差可以允许的范围
            break
        
    return theta0,theta1

def suiji (x,y,theta0,theta1,al,m,max):
    error=0
    k=0.0000001
    for j in range (max):
        m1,m2=0,0#
        for i in range(m):
            m1+=theta0+theta1*x[i]-y[i]#计算h[i]-y[i]
            m2+=(theta1*x[i]-y[i])*x[i]
       
            theta0-=(al/m)*m1#迭代更新,不断更新迭代知道迭代次数达到最大值或满足条件
            theta1-=(al/m)*m2
            
       
            
           
        for t in range(m):
            error+=(theta0+theta1*x[t]-y[t])**2  #计算误差
        if error<k:#判断是否误差可以允许的范围
            break
            
    return theta0,theta1


theta0,theta1= piliang (x,y,theta0,theta1,al,m,max)
theta2,theta3= suiji (x,y,theta0,theta1,al,m,max)
print("(批量梯度值) :{} {}". format(theta0,theta1))
print("（随机梯度）:{} {}". format(theta2,theta3))


print("继续等待散点图以及拟合的线性函数")
plt.scatter(x,y)
xx=np.linspace(0,12,30)


plt.title("the contact betwee YearsExperience and  salary")
plt.xlabel(" YearsExperience")
plt.ylabel("salary")
h1=theta1*xx+theta0
h2=theta3*xx+theta2
plt.plot(xx,h1,"r--",label="red:batch-green:random")
plt.plot(xx,h2,"g^")
plt.show()
print("红虚线代表批量梯度所得，绿三角石随机梯度所得）

#所得对比图像是：
[image](https://github.com/DL-Metaphysics/DL-molu-ggg/blob/master/%E5%B7%A5%E8%B5%84.png)

