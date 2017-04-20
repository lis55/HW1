# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:24:54 2017

@author: Carlos
"""

import numpy as np

FILEdata1 = open("data1.txt","r") 
FILEdata2 = open("data2.txt","r")
data1 = np.loadtxt(FILEdata1)
data2 = np.loadtxt(FILEdata2)

u1=data1[:,1]
u2=data1[:,2]
u3=data2[:,1]
u4=data2[:,2]
N=len(u1)
M=2000
n=int(N/M)
g_temp1=np.zeros(n)
U1=np.zeros(n)
U2=np.zeros(n)
U3=np.zeros(n)
U4=np.zeros(n)


unerror_u1=np.sqrt(1/N*np.mean(u1))
unerror_u2=np.sqrt(1/N*np.mean(u2))

print (unerror_u1)
print (unerror_u2)

for i in range(0,n):
    ji=i*M
    jf=(i+1)*M-1
    
    for j in range(ji,jf+1):
        g_temp1[i]=g_temp1[i]+u1[j]
        
    U1[i]=1/M*g_temp1[i]

r_error=np.sqrt(1/N*np.mean(U1))

print("question 3 %d",r_error)


M=2
n=int(N/M)
R_g_temp1=np.zeros(n)
g_temp1=np.zeros(n)
R_U1=np.zeros(n)
for i in range(0,n):  
    j_i=i*M+1
    j_f=(i+1)*M
    
    for j in range(j_i,j_f+1):
       R_g_temp1[i]=g_temp1[i]+u1[j]
        
    R_U1[i]=1/M*g_temp1[i]





