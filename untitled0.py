# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:25:05 2017

@author: Carlos
"""

import numpy as np

M=6
a=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
n=int(len(a)/M)
A=np.zeros(n)
a_temp=np.zeros(n)
print(a)
print(a_temp)
print(n)
print(M)
print(A)

for i in range(0,n):
    ji=i*M
    jf=(i+1)*M-1
    
    for j in range(ji,jf+1):
        a_temp[i]=a_temp[i]+a[j]
        
    A[i]=1/M*a_temp[i]

print (A)





