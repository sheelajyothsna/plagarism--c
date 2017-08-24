import os                                                           
import math
import string
import re
class plagiarism():                               # creating plagarism class
    def __init__(self):                       
        self
    def string(self,i):                           # creating method for class, 
        f=open(i,'r')
        p=str(f.read())
        p=p.lower()
        p=p.replace("\n","").replace(".","").replace(",","")
        p=re.sub('[@#$%^&*(){}?|/\:"-+=!~`;]','', p)
        #p=p.split(" ")
        print(p)
        return p
    def stringmatch(self,h,h1,a,b):
        lcs=0
        l3 = ''
        for i in range(a):
            for j in range(b):
                l2=""
                t=i
                while i<a and j<b and h[i]==h1[j]:
                    l2+=h[i]
                    i=i+1
                    j=j+1
             
                if len(l2)!=0:
                    le=len(l2)
                    if le>lcs:
                        lcs=le
                        l3= l2
                i=t
        #print(lcs)
        print (l3)
        return round(lcs)
    def res(self,t1,h,h1):
        print(h+h1)
        L1=(2*t1)/(h+h1)*100                           
        return L1 
    def intake(self):
        n=input('enter directory')
        z=os.listdir(n)
        print(z)
        os.chdir(n)
        L1=[]
        L2=[]
        for k in range(len(z)):
            for o in range(len(z)):
                if k==o:                                           # taking multiple files  and calling functions """              """printing outputs"""
                     L1.append("0")
                else:
                    h=c.string(z[k])
                    #print(str(h))
                    h1=c.string(z[o])
                    a=len(h)
                    #print(a)
                    b=len(h1)
                    try:
                        if a==0 and b==0:
                            raise Exception
                        else:
                            t1=(c.stringmatch(h,h1,a,b))
                            L1.append(str(c.res(t1,a,b))+'%')
                    except Exception:
                        L1.append("Empty")
            print(z[k],L1)
            L1=[]
c=plagiarism()
c.intake()










   
