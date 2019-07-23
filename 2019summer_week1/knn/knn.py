'''一组数据，根据一个人头发长短来确定预测该人的性别：
小明头发18cm，预测他的性别
（数据自己造的）'''

z2=[23,15,27,40,40,20]#z2为女生头发长度
z1=[6,20,12,3,16,15]#z1是男生头发长度
z=18#小明头发的长度
distance1,distance2=0,0
ls={}
k=5#k的设定
def knn(z1,z2,z,k):
    ls={}
    n=0
    
    for i in range(len(z1)):
        distance1=(z1[i]-z)**2#距离的计算
        distance2=(z2[i]-z)**2
         
        ls[distance1]=1
        ls[distance2]=2#采用字典的方式
    items=list(ls.items())####这一行代码不太清楚
    items.sort(reverse=True)
    for j in range(k):
        if items[i][1]==1:
            n+=1
    if n>3:
        print("he is a boy")
    else:
        print("she is a girl")   
knn(z1,z2,z,k)


'''运行结果：
k=3时，she is a girl
k=5时，she is a girl'''
