# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:51:22 2017

@author: Carlos
"""
# -- coding: utf-8 --
"""
Created on Wed Apr 12 23:24:54 2017

@author: Carlos
"""



import numpy as np
import math

def blocking(u, M):
	N=len(u)
	n=int(math.floor(N/(1.0*M)))
	g_temp=np.zeros(n)
	U=np.zeros(n)

	unerror_u=np.sqrt(1.0/N*np.var(u))

	print (unerror_u)

	for i in range(0,n):
	    ji=i*M
	    jf=(i+1)*M-1
	    
	    for j in range(ji,jf+1):
             g_temp[i]=g_temp[i]+u[j]
	
	    U[i]=1.0/M*g_temp[i]

	r_erroru=np.sqrt(1.0/N*np.var(U))

	print("question 3",r_erroru)
	return U

FILEdata1 = open("data1.txt","r") 
FILEdata2 = open("data2.txt","r")
data1 = np.loadtxt(FILEdata1)
data2 = np.loadtxt(FILEdata2)

u1=data1[:,1]
u2=data1[:,2]
u3=data2[:,1]
u4=data2[:,2]

N=len(u1)
unerror_u1=np.sqrt(1.0/N*np.var(u1))
unerror_u2=np.sqrt(1.0/N*np.var(u2))
unerror_u3=np.sqrt(1.0/N*np.var(u3))
unerror_u4=np.sqrt(1.0/N*np.var(u4))

M=2000
U1 = blocking(u1,M)
U2 = blocking(u2,M)
U3 = blocking(u3,M)
U4 = blocking(u4,M)

k=15
ep1=np.zeros(k)
ep2=np.zeros(k)
ep3=np.zeros(k)
ep4=np.zeros(k)
for x in range(1,k):
       
    M=2
    N=len(u1)
    u1 = blocking(u1,M)
    u2 = blocking(u2,M)
    u3 = blocking(u3,M)
    u4 = blocking(u4,M)

    ep1[x] = np.sqrt(1.0/N*np.var(u1))
    ep2[x] = np.sqrt(1.0/N*np.var(u2))
    ep3[x] = np.sqrt(1.0/N*np.var(u3))
    ep4[x] = np.sqrt(1.0/N*np.var(u4))

  
    
import matplotlib.pyplot as plt
plt.plot(ep1)
plt.savefig("ep1.png")





