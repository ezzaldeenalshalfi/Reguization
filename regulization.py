import numpy as num
import pandas as pan
import matplotlib.pyplot as py
xtr = num.array([1, 1.5, 2.3, 4, 5, 6, 7, 8, 9, 10])
ytr = num.array([3, 3.5, 4.5, 6, 6.5, 6.8, 7, 7, 7, 5])
xts = num.array([1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9])
yts = num.array([3, 3.5, 4.5, 6, 6.5, 6.8, 6.9, 7, 7, 7])

py.figure(figsize=(8, 2))
py.scatter(xtr, ytr, color='r')
py.scatter(xts, yts, color='b')
py.show()
xtr = xtr.reshape(-1, 1)
ytr = xtr.reshape(-1, 1)


class polyregression():
    def __init__(self, rate=0.001, iterations=1000, degree=2, lambda_v=0.002):
        self.rate = rate
        self.iterations = iterations
        self.degree = degree  # for the ploynomail features
        self.lambda_v = lambda_v

    def scale(self, x):
        xscale = x-num.mean(x, axis=0)  # to culcolate the emount of numbers
        xscale = xscale/num.std(xscale, axis=0)
        return xscale

    def transformation(self, xtr):
        self.n = xtr.shape[0]
        xtransformation = num.empty(self.n, 0)
        for j in range(self.degree + 1):
            if j != 0:
                xpower = num.power(xtr, j)  # to compute the first array
                xtransformation = num.append(xtransformation, xpower, axis=0)
            return xtransformation

    def fit(self, x, y):
            self.cost = []  # to create the empty arra
            self.theta = num.zeros((1+self.degree))  # one empty  [0,0,0]
            self.scale(x)
            xx = self.transformation(x)

            for i in range(self.iterations):  # to write the model of regulization
                ypre = self.theta[0]+num.dot(xx, self.theta[1:])
                ezz = self.lambda_v*num.sum(ypre.square(self.theta[1:]))
                mse = (1/self.n)*num.sum(num.square(ypre-y)**2)+ezz
                self.cost.append(mse)

                dtheta1 = (2/self.n)*num.dot(xx.T, (ypre-y))-ezz  # deravitive
                dtheta0 = (2/self.n)*num.sum(ypre-y)
                # value update
                self.theta[1:] = self.theta[1:]-self.rate*dtheta1
                self.theta[0] = self.theta[0]-self.rate*dtheta0
                return self

            def pre(self, x):  # to predict by using transform value
                x = self.scale(x)
                xx = self.transformation(x)
                # to predict a level
                return self.theta[0]+num.dot(xx, self.theta[1:])
                plr = polyregression()  # to create an object by using teh polylinearregression
                yptr = plr.pre(xtr)  # to predict the training examples
                ypts = plr.pre(xts)
                msetr = (1/xtr.shape[0])*num.sum((yptr-ytr))
                mstraining = num.sqrt(msert)
                msets = (1/yts.shape[0])*num.sum((ypts-yts))
                mstesting = num.sqrt(msets)
                print('Rmse Train=', mstraining)
                print('Rmse Testing=', mstesting)
    py.figure(figsize=(5, 2))
    py.scatter(xtr, ytr, label='Tr points',color='b')
    py.scatter(xts,yts,label='Ts points',color='r')
    py.plot(xtr,ytr,label='fitting line')
    py.plot(xts,yts,label='p line')
    py.legend(loc='upper left')
    py.show()
