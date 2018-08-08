import numpy as np
import matplotlib.pyplot as plt
import time

class TubuHosei():
    def __init__(self,f0,h,c,dt):
        self._f0 = f0
        self._h = h
        self._c = c
        self._dt = dt
        self.v()

    def v(self):
        h = self._h
        dt = self._dt
        dt2 = dt**2
        w=2.0*np.pi*self._f0
        w2 = w**2
        self._v= [1.0/(4.0*dt2*w2),
            h/(dt*w),
            1-1.0/(2.0*dt2*w2),
            -h/(dt*w),
            1.0/(4.0*dt2*w2)]
#         return self._v

    def Hosei(self,x):
        x1 = x / self._c
        return np.convolve(x1, self._v, 'same')

#     def Hosei(self,x):
#         dt = self._dt
#         f0 = self._f0
#         h = self._h
#         dt2 = dt**2
#         w=2.0*np.pi*f0
#         w2 = w**2
#         c= self._c
#         n=np.shape(x)[0]
#         y1=np.zeros(n)
#         x1=np.zeros(n+5)
#         x1[4:n+4]=x
#         x1 = x1 / c
#         for i in range(n):
# #             y1[i] = (x1[i]/(4.0*dt2) - h * w /dt * x1[i+1] + (w2- 1.0/(2.0*dt2))*x1[i+2]+
# #             h*w/dt*x1[i+3]+x1[i+4]/(4.0*dt2))/w2
#             y1[i] = (x1[i]/(4.0*dt2*w2) - h /(dt*w) * x1[i+1] + (1.0- 1.0/(2.0*dt2*w2))*x1[i+2]+
#             h/(dt*w)*x1[i+3]+x1[i+4]/(4.0*dt2*w2))
#         return y1


if __name__ == '__main__':

    f0=90
    h=0.27
    c=1.05
    freq=1000
    dt=1/freq
    tb = TubuHosei(f0,h,c,dt)
    print(tb._v)

#     v1 = tb.v()
#     t=np.arange(5)*dt
#     plt.subplot(5,1,1)
#     plt.plot(t,tb.v())

    n=4096
    t1=np.arange(n)*dt
    x1=np.zeros(n)
    x1[int(4096/2)] = float(n)
    plt.subplot(5,1,1)
    plt.plot(t1,x1)

    df = 1/(n * dt)
    f1 = np.arange(n)*df
    x2 = np.fft.fft(x1)/n
#     plt.subplot(5,1,2)
#     plt.plot(f1,np.abs(x2))

    t0 = time.time()
    x3 = tb.Hosei(x1)
    print(time.time()-t0)
    plt.subplot(5,1,2)
    plt.plot(t1,x3)

    x4 = np.fft.fft(x3)/n
    plt.subplot(5,1,3)
    plt.plot(f1,np.abs(x4))
    print(np.abs(x4)[0])

#     t0 = time.time()
#     x5 = tb.Hosei2(x1)
#     print(time.time()-t0)
#     x5=x5[0:n]
#     plt.subplot(5,1,2)
#     plt.plot(t1,x5)
#
#     x6 = np.fft.fft(x5)/n
#     plt.subplot(5,1,3)
#     plt.plot(f1,np.abs(x6))
#     print(np.abs(x6)[0])
    plt.show()


