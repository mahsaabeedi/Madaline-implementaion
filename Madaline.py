import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
t=[1,-1,-1,1]
v1=0.5
v2=0.5
b=0.5
w11=0.05
w12=0.1
w21=0.2
w22=0.2
b1=0.3
b2=0.15
finish=0
alpha=0.5
for epoch in range(10):
    x=0
    if finish!=1:
        for i in range(4):
            net1=(x1[i]*w11)+(x2[i]*w21)+b1
            if net1>=0:
                z1=1
            else:
                z1=-1
            net2=(x1[i]*w12)+(x2[i]*w22)+b2
            if net2>=0:
                z2=1
            else:
                z2=-1
            yin=(z1*v1)+(z2*v2)+b
            if yin>=0:
                y=1
            else:
                y=-1
            error=t[i]-y
            #print(error)
            if error!=0:
                if t[i]==1:
                    if abs(net1)<abs(net2):
                        w11=w11+(alpha*x1[i]*(1-net1))
                        w21=w21+(alpha*x2[i]*(1-net1))
                        b1=b1+(alpha*(1-net1))
                    elif abs(net2)<abs(net1):
                        w12=w12+(alpha*x1[i]*(1-net2))
                        w22=w22+(alpha*x2[i]*(1-net2))
                        b2=b2+(alpha*(1-net2))
                if t[i]==-1:
                    if net1>0:
                       w11=w11+(alpha*x1[i]*(-1-net1))
                       w21=w21+(alpha*x2[i]*(-1-net1))
                       b1=b1+(alpha*(-1-net1))
                    if net2>0:
                       w12=w12+(alpha*x1[i]*(-1-net2))
                       w22=w22+(alpha*x2[i]*(-1-net2))
                       b2=b2+(alpha*(-1-net2))
            else:
                x=x+1
                #print(x)
                if x==4:
                    finish=1
                    print("finish")
                    print("w11:",w11)
                    print("w21:",w21)
                    print("w12:",w12)
                    print("w22:",w22)
                    print("b1:",b1)
                    print("b2:",b2)
                    print("epoch:",(epoch+1))
                    
                    n = np.linspace(-1.5,1.5)
                    plt.plot(n,((-w11*n-b1)/w21))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.plot(n,((-w12*n-b2)/w22))
                    plt.scatter(x1,x2,s=4,marker='*',color='red')
                    plt.show()



