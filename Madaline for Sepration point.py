# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:35:01 2020

@author: Mahsa Abedi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:00:42 2020

@author: Mahsa Abedi
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# blue_point = np.array([[0,2] , [1,3.5], [1,1] ,[2,1],[2,2],[2,3],[3,1] ,[3,4],[4,2],[4,4]])
# blue_point = blue_point.reshape(10,2)

# x_red_point =np.random.normal(3,0.2,50)
# x_red_point=x_red_point.reshape(50,1)

# y_red_point =np.random.normal(2.5,0.3,50)
# y_red_point =y_red_point.reshape(50,1)

# red_point= np.concatenate((x_red_point,y_red_point),axis=1) 
# red_point=red_point.reshape(50,2)

# # red_blue =np.concatenate((blue_point,red_point), axis=0)
# #print(red_blue)

# # d=np.array([[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
#             # [-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
#             # [-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
#             # [-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
#             # [-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
#             # [-1],[-1],[-1],[-1],[-1]])


# # new_rb_lb_1=np.append(red_blue,d,axis=1)
# # new_rb_lb_1=new_rb_lb_1.reshape(60,3)
# # print(new_rb_lb_1)

# x_green_point =np.random.normal(1,0.2,50)
# x_green_point=x_green_point.reshape(50,1)
# y_green_point =np.random.normal(2,0.2,50)
# y_green_point=y_green_point.reshape(50,1)
# green_point= np.concatenate((x_green_point,y_green_point),axis=1)
# green_point=green_point.reshape(50,2)

# # c=np.ones((50,1))
# # new_green_point=np.append(green_point,c,axis=1)
# # new_green_point =new_green_point.reshape(50,3)

# #print(new_green_point)

# Q = np.concatenate((new_green_point,new_rb_lb_1),axis=0)
# # print(Q)

blue_point = [[0,2] , [1,3.5], [1,1] ,[2,1],[2,2],[2,3],[3,1] ,[3,4],[4,2],[4,4]]

x_red_point =np.random.normal(3,0.2,50)
x_red_point=x_red_point.reshape(50,1)
y_red_point =np.random.normal(2.5,0.3,50)
y_red_point =y_red_point.reshape(50,1)
red_point= np.concatenate((x_red_point,y_red_point),axis=1) 
red_point=red_point.reshape(50,2)


x_green_point =np.random.normal(1,0.2,50)
x_green_point=x_green_point.reshape(50,1)
y_green_point =np.random.normal(2,0.2,50)
y_green_point=y_green_point.reshape(50,1)
green_point= np.concatenate((x_green_point,y_green_point),axis=1)
green_point=green_point.reshape(50,2)

red_blue =np.concatenate((blue_point,red_point), axis=0)

dataset= np.concatenate((red_blue,green_point),axis=0)
c=np.ones((110,1))
dataset=np.append(dataset,c,axis=1)

v = dataset[:, :]   
dataset[:, :] = (v - v.min()) / (v.max() - v.min())

dataset = dataset.tolist()




v1 = 0.5
v2 = 0.5
v3 = 0.5
v4 = 0.5
# v5 = 0.5
# v6 = 0.5
# v7 = 0.5
# v8 = 0.5

# alpha = 0.05

w11=0
w12=0
w13=0
w14=0
# w15=0
# w16=0.1
# w17=0.1
# w18=0.1
# w19=0.1

# w21=0
# w22=0
# w23=0
# w24=0
# w25=0.2
# w26=0.2
# w27=0.2
# w28=0.2
# w29=0.2

# b1=0
# b2=0
# b3=0
# b4=0
# b5=0
# b6=0
# b7=0
# b8=0
# b9 = 1
# b10 =0.1


finish=0


# for epoch in range(50):
#     j=0
#     if finish!= 1:
#         for i in range(110):
#             net1=(Q[(i,0)]*w11)+(Q[(i,1)]*w21)+b1
#             if net1>=0:
#                 z1=1
#             else:
#                 z1=-1
#             #print(Z1)
            
#             net2=(Q[(i,0)]*w12)+(Q[(i,1)]*w22)+b2
#             if net2>=0:
#                 z2=1
#             else:
#                 z2=-1
#             #print(Z2)
            
#             net3=(Q[(i,0)]*w13)+(Q[(i,1)]*w23)+b3
#             if net3>=0:
#                 z3=1
#             else:
#                 z3=-1
#             #print(Z3)
            
#             net4=(Q[(i,0)]*w14)+(Q[(i,1)]*w24)+b4
#             if net4>=0:
#                 z4=1
#             else:
#                 z4=-1
#             #print(Z4)
            
#             # net5=(Q[(i,0)]*w15)+(Q[(i,1)]*w25)+b5
#             # if net5>=0:
#             #     z5=1
#             # else:
#             #     z5=-1
#             # #print(Z5)
            
#             # net6=(Q[(i,0)]*w16)+(Q[(i,1)]*w26)+b6
#             # if net6>=0:
#             #     z6=1
#             # else:
#             #     z6=-1
#             # #print(Z6)
            
#             # net7=(Q[(i,0)]*w17)+(Q[(i,1)]*w27)+b7
#             # if net7>=0:
#             #     z7=1
#             # else:
#             #     z7=-1
#             # #print(Z7)
            
#             # net8=(Q[(i,0)]*w18)+(Q[(i,1)]*w28)+b8
#             # if net8>=0:
#             #     z8=1
#             # else:
#             #     z8=-1
#             # #print(Z8)
            
#             # # net9=(Q[(i,0)]*w19)+(Q[i,1]*w29)+b1
#             # # Z9=activationfunction(net9)
#             # # #print(Z9)
            
#             # list =[abs(net1) ,abs(net2) ,abs(net3) , abs(net4) ,abs(net5) , abs(net6) , abs(net7) , abs(net8)]
#             # #print(min(list))
#             # min_list=min(list)
            
#             yin1=(z1*v1)*(z2*v2)*(z3*v3)*(z4*v4)*b9
#             # print(yin1)
#             if yin1>=0:
#                 y1=1
#             else:
#                 y1=-1
            
#             # yin2=(z5*v5)*(z6*v6)*(z7*v7)*(z8*v8)*-b10
#             # if yin2>=0:
#             #     y2=1
#             # else:
#             #     y2=-1
            
#             # if i<50:
#             #     
#             # else:
#             #     error=Q[(i,2)]-y2
            
#             error=Q[(i,2)]-y1 
#             if error!=0:
#                 if Q[(i,2)]==1:
#                     if net1<0:
#                         w11=w11+(alpha*Q[(i,0)]*(1-net1))
#                         w21=w21+(alpha*Q[(i,1)]*(1-net1))
#                         b1=b1+(alpha*(1-net1))
#                     if net2<0:
#                         w12=w12+(alpha*Q[(i,0)]*(1-net2))
#                         w22=w22+(alpha*Q[(i,1)]*(1-net2))
#                         b2=b2+(alpha*(1-net2))
#                     if net3<0:
#                         w13=w13+(alpha*Q[(i,0)]*(1-net3))
#                         w23=w23+(alpha*Q[(i,1)]*(1-net3))
#                         b3=b3+(alpha*(1-net3))
#                     if net4<0:
#                         w14=w14+(alpha*Q[(i,0)]*(1-net4))
#                         w24=w24+(alpha*Q[(i,1)]*(1-net4))
#                         b4=b4+(alpha*(1-net4))
                   
#                 if Q[(i,2)]==-1:
#                     if net1>0:
#                         w11=w11+(alpha*Q[(i,0)]*(-1-net1))
#                         w21=w21+(alpha*Q[(i,1)]*(-1-net1))
#                         b1=b1+(alpha*(-1-net1))
#                     if net2>0:
#                         w12=w12+(alpha*Q[(i,0)]*(-1-net2))
#                         w22=w22+(alpha*Q[(i,1)]*(-1-net2))
#                         b2=b2+(alpha*(-1-net2))
#                     if net3>0:
#                         w13=w13+(alpha*Q[(i,0)]*(-1-net3))
#                         w23=w23+(alpha*Q[(i,1)]*(-1-net3))
#                         b3=b3+(alpha*(-1-net3))
#                     if net4>0:
#                         w14=w14+(alpha*Q[(i,0)]*(-1-net4))
#                         w24=w24+(alpha*Q[(i,1)]*(-1-net4))
#                         b4=b4+(alpha*(-1-net4))      
#             else:
#                 j=j+1
#                 print(j)
#                 if j==110:
#                     finish=1
#                     print("finish")
#                     print("w11:",w11)
#                     print("w21:",w21)
#                     print("w12:",w12)
#                     print("w22:",w22)
#                     print("w13:",w13)
#                     print("w14:",w14)
#                     print("b1:",b1)
#                     print("b2:",b2)
#                     print("epoch:",(epoch+1))
                    
                    
#                     plt.figure()
#                     ax1=plt.subplot(1,1,1)
#                     n = np.linspace(-1,1)
#                     plt.plot(n,((-w11*n-b1)/w21))
#                     plt.plot(n,((-w12*n-b2)/w22))
#                     plt.plot(n,((-w13*n-b3)/w23))
#                     plt.plot(n,((-w14*n-b4)/w24))
#                     # plt.plot(n,((-w15*n-b5)/w25))
#                     # plt.plot(n,((-w16*n-b6)/w26))
#                     # plt.plot(n,((-w17*n-b7)/w27))
#                     # plt.plot(n,((-w18*n-b8)/w28))
#                     plt.scatter(x_red_point,y_red_point,s=10,marker='.',color='red')
#                     plt.scatter(x_green_point,y_green_point,s=10,marker='.',color='green')
#                     plt.scatter([0,1,1,2,2,2,3,3,4,4],[2,3.5,1,1,2,3,1,4,2,4],marker='.',color='blue')
#                     ax1.plot()
#                     plt.show()
                    
                    
                    
#                      # if net5<0:
#                     #    w15=w15+(alpha*Q[(i,0)]*(1-net5))
#                     #    w25=w25+(alpha*Q[(i,1)]*(1-net5))
#                     #    b5=b5+(alpha*(1-net5))
#                     # if net6<0:
#                     #    w16=w16+(alpha*Q[(i,0)]*(1-net6))
#                     #    w26=w26+(alpha*Q[(i,1)]*(1-net6))
#                     #    b6=b6+(alpha*(1-net6))
#                     # if net7<0:
#                     #    w17=w17+(alpha*Q[(i,0)]*(1-net7))
#                     #    w27=w27+(alpha*Q[(i,1)]*(1-net7))
#                     #    b7=b2+(alpha*(1-net7))
#                     # if net8<0:
#                     #    w18=w18+(alpha*Q[(i,0)]*(1-net8))
#                     #    w28=w28+(alpha*Q[(i,1)]*(1-net8))
#                     #    b8=b8+(alpha*(1-net8))
                        
                    
