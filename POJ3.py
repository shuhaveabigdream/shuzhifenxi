from functools import reduce
import numpy as np
import matplotlib.pyplot as plot
import operator

def prod(factors):
    return reduce(operator.mul, factors, 1)
#由唯一性得  管球的你用的啥子插值法  得到得插值多项式是唯一的
class Lagrange:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass
    def Function(self,x):
        fenmu=[]
        fenzi=[]
        for i in range(len(self.x)):
            tmp=[]
            tmp1=[]
            for j in range(len(self.x)):
                if i!=j:
                  tmp.append(self.x[i]-self.x[j])
                  tmp1.append(x-self.x[j])
            fenmu.append(prod(tmp))
            fenzi.append(prod(tmp1))
        return sum([self.y[i]*(fenzi[i]/fenmu[i]) for i in range(len(self.x))])


class Newton(Lagrange):
    def __init__(self,x,y,function):
        super(Newton,self).__init__(x,y)
        self.function=function
    def GetQuot(self,lenth):
        if lenth==0:
            return function(self.x[0])
        buffer=[]
        for i in range(lenth):
            tmp=1
            for j in range(lenth):
                if i!=j:
                    tmp*=self.x[i]-self.x[j]
            buffer.append(self.function(self.x[i])/tmp)
        return sum(buffer)

    def Fcuntion(self,x):
        res=0
        for i in range(len(self.x)-1):
            quot=self.GetQuot(i)
            param=prod([x-self.x[j] for j in range(len(self.x)-1)])
            res+=quot*param
        return res


#限定为5次
class LinerFitter:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.Xmatrix=None
        self.Ymatrix=None
        self.params=None
    def GetMatrixs(self):
        matrix=[]
        matrix=[[item**t for t in range(6)] for item in self.x]
        self.Xmatrix = np.array(matrix,dtype=float)
        Xtranpose=np.transpose(self.Xmatrix)
        self.Ymatrix = np.transpose(np.array([self.y], dtype=float))
        self.Ymatrix=Xtranpose.dot(self.Ymatrix)
        self.Xmatrix=Xtranpose.dot(self.Xmatrix)
    def GetParams(self):
        self.params=np.linalg.inv(self.Xmatrix).dot(self.Ymatrix)
    def Fire(self,x):
        x_matrix=np.array([[x**t for t in range(6)]],dtype=float)
        y=x_matrix.dot(self.params)
        return y
def Get_Points(function,n):
    points=[(2*i)/n-1 for i in range(0,n+1)]
    print('points',points)
    y=[function(x) for x in points]
    return points,y

def function(x):
    return 1/(1+25*(x**2))

if __name__=="__main__":
    n=8
    x, y = Get_Points(function, n)
    print('x',x)
    print('y',y)
    test_x = np.linspace(x[0], x[-1], 1000)

    test_y=[function(i) for i in test_x]
    plot.plot(test_x,test_y,'b')

    obj=Lagrange(x,y)
    y=[obj.Function(i) for i in test_x]
    plot.plot(test_x,y,'r')
    plot.savefig("./Newton/newton%d.jpg"%n)
    plot.title('using Newtoniter n=%d'%n)
    plot.show()

    """
    obj=LinerFitter(x,y)
    obj.GetMatrixs()
    obj.GetParams()
    y = [obj.Fire(i)[0][0] for i in test_x]
    plot.plot(test_x, y, 'r')
    plot.savefig("./Newton/newton%d.jpg" % n)
    plot.title('using Newtoniter n=%d' % n)
    plot.show()
"""