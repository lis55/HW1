# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:06:00 2017

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


	return U

FILEdata1 = open("data1.txt","r") 
FILEdata2 = open("data2.txt","r")
data1 = np.loadtxt(FILEdata1)
data2 = np.loadtxt(FILEdata2)


u1=data1[:,1]
u2=data1[:,2]
u3=data2[:,1]
u4=data2[:,2]

M=2000

u1 = blocking(u1,M)
u2 = blocking(u2,M)
u3 = blocking(u3,M)
u4 = blocking(u4,M)
n=len(u1)


gJ1=np.zeros(n)
gJ2=np.zeros(n)
gJ3=np.zeros(n)
gJ4=np.zeros(n)
for i in range(0,n):
    gJ1[i]=(1.0/(n-1))*(np.sum(u1)-u1[i])
    gJ2[i]=(1.0/(n-1))*(np.sum(u2)-u2[i])
    gJ3[i]=(1.0/(n-1))*(np.sum(u3)-u3[i])
    gJ4[i]=(1.0/(n-1))*(np.sum(u4)-u4[i])

    
RJ21=np.zeros(n)
RJ31=np.zeros(n)
RJ41=np.zeros(n)
for i in range(0,n):
    RJ21[i]=gJ2[i]/gJ1[i]
    RJ31[i]=gJ3[i]/gJ1[i]
    RJ41[i]=gJ4[i]/gJ1[i]
    
R21=np.mean(u2)/np.mean(u1)
R31=np.mean(u3)/np.mean(u1)
R41=np.mean(u4)/np.mean(u1)
RJK21=n*R21-((n-1.0)/n)*np.sum(RJ21)
RJK31=n*R31-((n-1.0)/n)*np.sum(RJ31)
RJK41=n*R41-((n-1.0)/n)*np.sum(RJ41)

a21=0
a31=0
a41=0
for i in range(0,n):
    a21=a21+np.power((RJ21[i]-RJK21),2)
    a31=a31+np.power((RJ31[i]-RJK31),2)
    a41=a41+np.power((RJ41[i]-RJK41),2)

errorJK21=np.sqrt((n-1)*1.0/n*a21)
errorJK31=np.sqrt((n-1)*1.0/n*a31)
errorJK41=np.sqrt((n-1)*1.0/n*a41)

print(errorJK21)
print(errorJK31)
print(errorJK41)
