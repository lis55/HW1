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
g_temp2=np.zeros(n)
g_temp3=np.zeros(n)
g_temp4=np.zeros(n)
U1=np.zeros(n)
U2=np.zeros(n)
U3=np.zeros(n)
U4=np.zeros(n)


unerror_u1=np.sqrt(1/N*np.var(u1))
unerror_u2=np.sqrt(1/N*np.var(u2))
unerror_u3=np.sqrt(1/N*np.var(u3))
unerror_u4=np.sqrt(1/N*np.var(u4))

print (unerror_u1)
print (unerror_u2)
print (unerror_u3)
print (unerror_u4)

for i in range(0,n):
    ji=i*M
    jf=(i+1)*M-1
    
    for j in range(ji,jf+1):
        g_temp1[i]=g_temp1[i]+u1[j]
        g_temp2[i]=g_temp2[i]+u2[j]
        g_temp3[i]=g_temp3[i]+u3[j]
        g_temp4[i]=g_temp4[i]+u4[j]
        
    U1[i]=1/M*g_temp1[i]
    U2[i]=1/M*g_temp2[i]
    U3[i]=1/M*g_temp3[i]
    U4[i]=1/M*g_temp4[i]

r_erroru1=np.sqrt(1/N*np.var(U1))
r_erroru2=np.sqrt(1/N*np.var(U2))
r_erroru3=np.sqrt(1/N*np.var(U3))
r_erroru4=np.sqrt(1/N*np.var(U4))

print("question 3",r_erroru1)
print("question 3",r_erroru2)
print("question 3",r_erroru3)
print("question 3",r_erroru4)


k=6
ep1=np.zeros(k)
ep2=np.zeros(k)
ep3=np.zeros(k)
ep4=np.zeros(k)
for x in range(1,k):
       
    M=2
    n=int(len(u1)/M)
    R_g_temp1=np.zeros(n)
    g_temp1=np.zeros(n)
    g_temp2=np.zeros(n)
    g_temp3=np.zeros(n)
    g_temp4=np.zeros(n)
    R_U1=np.zeros(n)
    R_U2=np.zeros(n)
    R_U3=np.zeros(n)
    R_U4=np.zeros(n)
    
    for i in range(0,n):  
        ji=i*M
        jf=(i+1)*M-1
        
        for j in range(ji,jf+1):
            g_temp1[i]=g_temp1[i]+u1[j]
            g_temp2[i]=g_temp2[i]+u2[j]
            g_temp3[i]=g_temp3[i]+u3[j]
            g_temp4[i]=g_temp4[i]+u4[j]
            
        R_U1[i]=1/M*g_temp1[i]
        R_U2[i]=1/M*g_temp2[i]
        R_U3[i]=1/M*g_temp3[i]
        R_U4[i]=1/M*g_temp4[i]
    
    ep1[x]=nerror_u1=np.sqrt(1/N*np.var(R_U1))
    ep2[x]=nerror_u2=np.sqrt(1/N*np.var(R_U2))
    ep3[x]=nerror_u3=np.sqrt(1/N*np.var(R_U3))
    ep4[x]=nerror_u4=np.sqrt(1/N*np.var(R_U4))
        
    print(nerror_u1)
    print(nerror_u2)
    print(nerror_u3)
    print(nerror_u4)
    
    u1=R_U1
    u2=R_U2
    u3=R_U3
    u4=R_U4
    
import matplotlib.pyplot as plt
plt.plot(ep1,[0,1,2,3,4,5,6,7,8,9])
    





