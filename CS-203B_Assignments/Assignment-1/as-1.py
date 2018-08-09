#!/usr/bin/python
import random as r
import numpy as np
import matplotlib.pyplot as plt
import sys
from tqdm import tqdm

def best_candidate_selection(array, l, k, mx):
 tempmx_k=array[0,0]
 for i in range(k):
  if array[0,i]>tempmx_k:
   tempmx_k=array[0,i]
 if tempmx_k == mx:
  return 0
 for j in range(k,l):
  if array[0,j] > tempmx_k and array[0,j] != mx:
   return 0
  elif array[0,j] == mx:
   return 1
 return 1
  
 
#n=[10]
n=[100,200,300,400,500,600,700,800,900,1000]
prob_kn=[]
val_k=[]
f=open("table.txt","w")
f.write("Table for values of k v/s P_kn for n = 1000\n")
f.write("k  P_kn\n")
f1=open("maximum_val.txt","w")
f1.write("Table for values of maximum k and P_kn for each n\n")
f1.write("n  k_max  P_kn_max\n")
  
for i in tqdm(n[:]):
 arr=np.random.random_sample((1,i))
 #print arr
 maxm=arr[0,0]
 prob_maxm=0
 value_maxm=0
 prob_count=np.zeros((1,i),dtype=float)

 for x in range(i):
  if arr[0,x]>maxm:
   maxm=arr[0,x]

 for j in range(0,1000):
  arr=arr.reshape((i,1))
  #print j
  arr=np.random.permutation(arr)
  arr=arr.reshape((1,i))
  

  for k in range(0,i):
   prob_count[0,k]=prob_count[0,k] + best_candidate_selection(arr, i, k, maxm)
   if i==1000 and j==999:
    #print 1
    prob_kn.append(prob_count[0,k])
    val_k.append(k)
    f=open("table.txt","a")
    f.write("%d  %f\n" %(k,(prob_count[0,k]/1000)))
    
 for y in range(i):
   if prob_count[0,y] > prob_maxm:
    prob_maxm=prob_count[0,y]
    value_maxm=y
   
 f1=open("maximum_val.txt","a")
 f1.write("%d  %d  %f\n" %(i,value_maxm,(prob_maxm/1000))) 

plt.plot(val_k,prob_kn,'ro-')
plt.xlabel('Value of k')
plt.ylabel('Probability P_kn')
plt.title('Graph of k v/s P_kn for n = 1000')
plt.text(10,0.8,r'$n = 1000$')
plt.axis([0,1000,0,1])
plt.grid(True)
plt.savefig('graph.pdf')
f.close()
f1.close()
