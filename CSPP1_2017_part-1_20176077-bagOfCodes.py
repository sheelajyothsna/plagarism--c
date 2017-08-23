import os                                                           
import math
class plagiarism():
    def __init__(self):
        self
    def dict(self,i):
        d={}
        f=open(i,'r')                                                                #creating dictionary function
        p=str(f.read())
        p=p.lower()
        p=p.replace("\n"," ").replace("\t"," ").replace("."," ").replace(","," ")
        p=p.split(" ")
        
        for k in p:
                if k not in d:                                   # counting no of values and storing in dictionary """
                    d[k]=1
                else:
                    d[k]+=1
        if '' in d:
            del d['']
        f.close()
        return d
    def dot_num(self,d1,d2):
        w=0
        for k in d1:
            for o in d2:                                        # dot product of frequencies """
                if k==o:
                    u=(d1[k]*d2[o])
                    w=w+u
        return w
    def eucild(self,x,y):
        p1=0
        p2=0                                                       # eucildian product"""
        for k in x:
            p1+=(x[k])**2
        for k in y:
            p2+=(y[k])**2
            
        p1=math.sqrt(p1)
        p2=math.sqrt(p2)
        return p1*p2
         
    def res(self,w,v):
        L1=(round((w/v)*100))                            #distance calculation """
        if L1==0:
            return 1.57
        return L1 
    def intake(self):
        n=input('enter directory')
        z=os.listdir(n)
        os.chdir(n)
        t=[]
        L1=[]
        for k in range(len(z)):
            for o in range(len(z)):
                if k==o:                                           # taking multiple files  and calling functions """              """printing outputs"""
                     L1.append("0")
                else:
                    t.append(c.dict(z[k]))
                    t.append(c.dict(z[o]))
                    g1=c.dot_num(t[0],t[1])
                    e=c.eucild(t[0],t[1])
                    L1.append(str(c.res(g1,e))+'%')
                
                    t=[]
            #print(z[k])
            print(L1)
            L1=[]
c=plagiarism()
c.intake()










   
