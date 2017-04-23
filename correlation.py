# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:23:38 2017

@author: Carlos
"""

import numpy as np
import math
import matplotlib.pyplot as plt

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
C1=np.zeros(100)
for n in range (0,100):
    for k in range(0,N-n):
        C1[n]=C1[n]+((u1[k+n]-np.mean(u1))*(u1[k]-np.mean(u1)))
        
    C1[n]=(1.0/(N-n))*C1[n]
        
plt.plot(C1)
        