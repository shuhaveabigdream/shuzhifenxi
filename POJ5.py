import numpy as np

class Romberg:
    def __init__(self,top,down,function,errval):
        self.top=top
        self.down=down
        self.function=function
        self.h=top-down
        self.T=[]
        self.T.append(self.h*(function(top)-function(down))/2)#this is T1
        self.k=0
        self.errval=errval
        self.evp=errval+1
        self.step=0
    def looper(self):
        S=[]
        C=[]
        R=[]
        while self.errval<self.evp:
            self.step += 1
            self.k = self.k + 1
            t = 0
            for i in range(2 ** (self.k - 1) - 1):
                t = t + self.function(self.down + (2 * (i + 1) - 1) * self.h / 2 ** self.k) * self.h / 2 ** self.k
            t = t + self.T[-1] / 2
            self.T.append(t)
            if self.k >= 1:
                S.append((4 ** self.k * self.T[-1] - self.T[-2]) / (4 ** self.k - 1))
            if self.k >= 2:
                C.append((4 ** self.k * S[-1] - S[-2]) / (4 ** self.k - 1))
            if self.k >= 3:
                R.append((4 ** self.k * C[-1] - C[-2]) / (4 ** self.k - 1))
            if self.k > 4:
                self.evp = abs(10 * (R[-1] - R[-2]))
        return R[-1]
    def fire(self):
        return self.looper(),self.step

class Gauss:
    def __init__(self,func,n,m,a,b):
        self.function=func
        self.n=n#分点数
        self.m=m#分段数
        self.h=(b-a)/m
        self.area=[a,a+h]
        self.params={}
        self.params['n=1']=[[0.5773503],[1]]
        self.params['n=2']=[[0.7745967,0],[0.5555556,0.8888889]]
        self.params['n=3']=[[0.8611363,0.339981],[0.3478548,0.6521452]]
        self.params['n=4']=[[0.9061798,0.5384693,0],[0.2369269,0.4786287,0.5688889]]
        self.params['n=5']=[[0.9324695,0.6612094,0.2386192],[0.1713245,0.3607616,0.4679139]]
        self.kval=self.params['n=%d'%self.n]
        self._res=0.0

    def Area(self):
        self.area[0]+=self.h
        self.area[1]+=self.h
        if self.area[1]>self.b:
            return None
        return self.area
    def looper(self):
        x = self.kval[0]
        A=self.kval[1]
        for i in range(len(x)):
            self._res+=self.function(x[i])*A[i]
            if x[i]==0:
                pass
            else:
                self._res+=self.function(-x[i])*A[i]
    def Fire(self):
       self.looper()
       return self._res

def function(x):
    return 8/(4+(x+1)**2)


if __name__=="__main__":
    obj = Romberg(1, 0, lambda x:4/(x**2+1),0.01)
    res,step=obj.fire()
    print('rombreg res',res,'step',step)
    for i in range(1,6):
        obj = Gauss(function,i,4,0,1)
        res=obj.Fire()
        print('Gauss res n=%d'%i,res)