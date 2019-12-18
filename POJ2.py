#目标找出LU
#model:A=LU
import numpy as np

class Doolittle:
    def __init__(self,A):
        self.A=A
        self.shape=A.shape
        self.U=np.zeros(self.shape,dtype=int)
        self.L=np.zeros(self.shape,dtype=int)
        self.lines=A.shape[0]
        for i in range(self.lines):
            self.U[0][i]=self.A[0][i]
            self.L[i][0]=self.A[i][0]/self.U[0][0]
    def Fire(self):
        #先算u的行再算L的列
        for r in range(1,self.lines):
            for i in range(r,self.lines):#行运算
                self.U[r][i]=self.A[r][i]-sum([self.L[r][k]*self.U[k][i] for k in range(0,r)])
            for i in range(r,self.lines):#列运算
                self.L[i][r]=(self.A[i][r]-sum([self.L[i][k]*self.U[k][r] for k in range(0,r)]))/self.U[r][r]
        return self.L,self.U
    def check(self):
        print(' L*U=',self.L.dot(self.U))
    def GetUL(self):
        return self.U.dot(self.L)
if __name__=="__main__":
    A=np.array([[1,2,3],[2,5,2],[3,1,5]],dtype=int)
    for i in range(2000):
        obj = Doolittle(A)
        L,U=obj.Fire()
        A=obj.GetUL()
        if i%50==0:
            print(A)
