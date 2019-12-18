import numpy as np
import copy

inputD=0

if inputD:
    EampleArry = np.array([
                           [1,2,-2],
                           [1,1,1],
                           [2,2,1]
                           ])
    BArray=np.array([7,2,5])
else:
    EampleArry = np.array([
                          [2, -1, 1],
                          [2, 2, 2],
                          [-1, -1, 2]
    ])
    BArray = np.array([-1,4,-5])

class Jacobi:
    def __init__(self,A,b,x,e):
        self.tmp_x=np.array([0,0,0],dtype=float)
        self.e=e
        self.b=b
        self.x=x
        self.A=A
        self.times=0
        shape=A.shape
        if shape[0]!=shape[1]:
            raise ValueError("check the shape of matrix")
        self.D=np.zeros(shape,dtype=int)
        self.L=np.zeros(shape,dtype=int)
        self.U=np.zeros(shape,dtype=int)
        lines=shape[0]
        self.lines =lines
        for i in range(lines):
            self.D[i][i]=A[i][i]
        for i in range(lines):
            for j in range(lines):
                if j<i:
                    self.L[i][j]=-A[i][j]
                elif j>i:
                    self.U[i][j]=-A[i][j]
        self.flag=True
    def GetFunction(self):
        if self.Dirct()==False:
            print('该矩阵不收敛')
            return None
        return self.__looper
    def GetXi(self,i):
        array=list(range(0,self.lines))
        array.remove(i)
        tmp=self.b[i]-sum([self.A[i][j]*self.x[j] for j in array])
        return tmp/self.A[i][i]
    #判断是否收敛
    def Dirct(self):
        Dl=np.linalg.inv(self.D)
        Mj= Dl.dot(self.L+self.U)
        res=np.linalg.eig(Mj)
        features=[np.abs(i) for i in res[0]]
        features=np.sort(features)
        return features[-1]<1

    def __looper(self):
        tmp=copy.deepcopy(self.x)
        if self.flag==True:
            for i in range(self.lines):
              self.tmp_x[i]=self.GetXi(i)
            self.x=copy.deepcopy(self.tmp_x)
        else:
            for i in range(self.lines):
              self.x[i]=self.GetXi(i)
        val=tmp-self.x
        if ((tmp-self.x>-self.e).all() and (tmp-self.x<self.e).all())==True or self.times>400:
            print('backtracert',self.times)
            print('self.x',self.x)
            return self.x
        else:
            self.times+=1
            self.__looper()

class Gauss(Jacobi):
    def __init__(self,A,b,x,e):
        super(Gauss,self).__init__(A,b,x,e)
        self.flag=False#实时更新
    def Dirct(self):
        Mg= np.linalg.inv((self.D-self.L)).dot(self.U)
        res = np.linalg.eig(Mg)
        features = [np.abs(float(i)) for i in res[0]]
        features = np.sort(features)
        return features[-1] < 1
    def GetXi(self,i):
        tmp=self.b[i]\
            -sum([self.A[i][j]*self.x[j] for j in range(0,i)])\
            -sum([self.A[i][j]*self.x[j] for j in range(i+1,self.lines)])
        return tmp/self.A[i][i]


if __name__=="__main__":
    print('using Jacobi')
    jac=Jacobi(
             EampleArry,
             BArray,
             np.array([0,0,0],dtype=float),
             np.array([0.0000001, 0.0000001, 0.00000001], dtype=float),
    ).GetFunction()

    if jac:
        jac()
    else:
        print("jacco dosen't work")
    print('------------------------')
    print('using Gauss')
    Gau=Gauss(
             EampleArry,
             BArray,
             np.array([0,0,0],dtype=float),
             np.array([0.000001,0.0000001,0.0000001],dtype=float),
                      ).GetFunction()
    if Gau:
        Gau()
    else:
        print("Gassus doesn't work")
