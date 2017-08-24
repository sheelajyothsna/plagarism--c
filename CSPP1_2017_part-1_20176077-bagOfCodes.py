import os                                                           
import math
import string
import re
class plagiarism():
    def __init__(self):
        self
    def dict(self,i):
        d={}
        f=open(i,'r')                                                                #creating dictionary function
        p=str(f.read())
        p=p.lower()
        p=p.replace("\n"," ").replace("\t"," ").replace("."," ").replace(","," ")
        p=re.sub('[@#$%^&*(){}?|/\:"-+=!~`;]','', p)
        p=p.split(" ")
        #p=[i.strip(string.punctuation)for i in p]
        
        for k in p:
                if k in d:                                   # counting no of values and storing in dictionary """
                    d[k]+=1
                else:
                    d[k]=1
        if '' in d:
            del d['']
        #print(d)
        f.close()
        return d
    def dot_num(self,d1,d2):
        w=0
        for k in d1:
            for o in d2:                                        # dot product of frequencies """
                if k==o:
                    w+=(d1[k]*d2[o])
                    
        return w
    def eucild(self,x):                                                       # eucildian product"""
        p1=0
        for k in x:
            p1+=(x[k])**2
            
        p1=math.sqrt(p1)
        return p1
         
    def res(self,w,v):
        #print(w)
        #print(v)
        L1=(((w/v)*100))                            #distance calculation """
        if L1==0:
            return 1.57
        return round(L1,2) 
    def intake(self):
        n=input('enter directory')
        z=os.listdir(n)
        os.chdir(n)
        L1=[]
        for k in range(len(z)):
            for o in range(len(z)):
                if k==o:                                           # taking multiple files  and calling functions """              """printing outputs"""
                     L1.append("0")
                else:
                    t1=(c.dict(z[k]))
                    print(t1)
                    t2=(c.dict(z[o]))
                    print(t2)
                    g1=c.dot_num(t1,t2)
                    e1=c.eucild(t1)
                    e2=c.eucild(t2)
                    e=e1*e2
                    L1.append(str(c.res(g1,e))+'%')
            print(z[k])
            print(L1)
            L1=[]
c=plagiarism()
c.intake()










   
