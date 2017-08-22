import os
import math
def dict(i):
    l=[]
    d={}
    f=open(i,'r')
    for line in f:
        for word in line.split():
            p=word.lower()
            p=p.replace(","," ").replace("."," ").replace("\n"," ")
            l.append(p)
    for i in l:
        if i=='':
            pass
        elif i not in d:
            d[i]=1
        else:
            d[i]+=1
        
    f.close()
    return d
def dot_num(d1,d2):
    w=0
    for k in d1:
        for o in d2:
            if k==o:
                u=(d1[k]*d2[o])
                w=w+u
    return w
def eucild(x,y):
    p1=0
    p2=0
    for k in x:
        p1+=(x[k])**2
    for k in y:
        p2+=(y[k])**2
        
    p1=math.sqrt(p1)
    p2=math.sqrt(p2)
    return p1*p2
     
def res(w,v):
    L1=round((w/v)*100)
    if L1==0:
        return 1.57
    return L1
n=input('enter directory')
z=os.listdir(n)
os.chdir(n)
t=[]
L1=[]
for k in range(len(z)):
    for o in range(len(z)):
        if k==o:
            L1.append("pilla")
        else:
            t.append(dict(z[k]))
            t.append(dict(z[o]))
            g1=dot_num(t[0],t[1])
            e=eucild(t[0],t[1])
            L1.append(res(g1,e))
            
            t=[]
    print(z[k])
    print(L1)
    L1=[]








   
