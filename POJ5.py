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
    def looper(self):
        S=[]
        C=[]
        R=[]
        while self.errval<self.evp:
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
        return self.looper()



if __name__=="__main__":
    obj=Romberg(1,0,lambda x:x**2,0.001)
    res=obj.fire()
    print('res',res)