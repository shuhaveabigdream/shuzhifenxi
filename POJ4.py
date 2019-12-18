import numpy as np

class iteration:
    def __init__(self,function,err_value,start):
        self.steps=[]
        self.function=function
        self.err_value=err_value
        self.x=start
        self.times=0
        self.steps.append(start)
        self.L=self.Get_L()
    def compare(self,x,y):
        if ("%.04f"%x).split('.')[1][3]==("%.04f"%y).split('.')[1][3]:
            return True
        return False
    def compareWithDif(self,x):
        return self.GetDif1() if x else self.GetDif2()
    def looper(self,x):
        self.times+=1
        lx=self.function(x)
        self.steps.append(lx)
        return "%.04f"%lx if self.compareWithDif(1)==True else self.looper(lx)
    def Get_L(self):
        test_point=np.linspace(self.x-0.5,self.x+0.5,100)
        max_value=0.0
        for i in range(len(test_point)-1):
            max_value=max(max_value,np.abs((self.function(test_point[i+1])-self.function(test_point[i]))/(test_point[i+1]-test_point[i])))
        return max_value
    def GetDif1(self):
        return np.abs((self.L/(1-self.L))*(self.steps[-1]-self.steps[-2]))<0.0001
    def GetDif2(self):
        return np.abs((self.L**self.times)/(1-self.L)*(self.steps[1]-self.steps[0]))<0.0001
    def Fire(self):
        return self.looper(self.x),self.times


if __name__=="__main__":
    obj=iteration(lambda x:(x**2+1)**(1/3),0.0001,1.5)
    print('res',obj.Fire())
    print('L',obj.Get_L())
