
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

class CurveFit():
    def __init__(self,x=None,y=None,x0=np.array([0.,0.,0.,])):
        self._x = x
        self._y = y
        self._x0 = x0

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x):
        self._x = x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        self._y = y
    @property
    def x0(self):
        return self._x0
    @x0.setter
    def x0(self, x0):
        self._x0 = x0
    @property
    def result(self):
        return self._result[0]

    def Calc(self):
        self._result = optimize.leastsq(self.fun,self._x0,args=(self._x,self._y))
        return self._result[0]

    def model(self,x, u):
        return x[2]*x[0]**2 /((x[0]**2 - u**2)**2 + 4 * u**2 * x[0]**2 * x[1]**2)**0.5
#         return x[0]**2 /((x[0]**2 - u**2)**2 + 4 * u**2 * x[0]**2 * x[1]**2)**0.5

    def fun(self,x, u, y):
        return  y - self.model(x, u)

    def ydata(self,xdata=None):
        return self.model(self.result,xdata)

    def PhaseData(self,xdata=None):
        h=self._result[0][1]
        w=self._result[0][0]
        p=np.arctan((2*h*xdata/w)/(1.0-(xdata/w)**2)) * -180/(np.pi)
        n=p.shape[0]
        pp=np.zeros(n)
        for i in range(n):
            if p[i]>0:
                pp[i]=p[i]-180
                if pp[i]<-180:
                    pp[i]=pp[i]+360
            else:
                pp[i]=p[i]

        return pp

if __name__ == '__main__':
#     u = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
#     y = np.array([1.05,1.06026,1.09209,1.14877,1.23642,1.36471,1.54637,1.78857,2.0518,2.16653,1.95426,1.56304,1.20954,0.946933,0.758578,0.621689,0.519693,
#     0.441726,0.380731,0.332039,0.292485])

#     u = np.load('freq - Copy.npy')
    u = np.load('freq.npy')
    print(u)
#     y = np.load('amp - Copy.npy')
    y = np.load('amp.npy')
    print(y[:,0])
#     nmax=np.argmax(y[1:500,0])-1
    nmax = int(np.argmax(y[:,0])*1.10)
    print(nmax)

    u1 = u[1:nmax]
    y1 = y[1:nmax,0]
#     y = y[:,0]
    plt.subplot(4,1,1)
    plt.plot(u,y[:,0])

    x0=np.array([100,1.0,2.0])

    cf = CurveFit(u1,y1,x0)
    r1 = cf.Calc()
    print(cf.result)
    u1=u
#     plt.plot(u,y,'o')
    plt.plot(u1,cf.ydata(u1))

    plt.subplot(4,1,2)
    plt.plot(u1,cf.PhaseData(u1))
    plt.show()