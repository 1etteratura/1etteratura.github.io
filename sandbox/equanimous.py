import numpy as n

class Equanimous:
    def __init__(self, dxy=1, dxz=1, dyx=1, dyz=1, dzx=1, dzy=1, x=1, y=1, z=1):
        self.dxy = dxy
        self.dxz = dxz

        self.dyx = dyx
        self.dyz = dyz

        self.dzx = dzx
        self.dzy = dzy

        self.x = x
        self.y = y
        self.z = z

    def px(self, x):
        return x + self.dxy * self.y + self.dxz * self.z

    def py(self, y):
        return y + self.dyx * self.x + self.dyz * self.z

    def pz(self, z):
        return z + self.dzx * self.x + self.dzy * self.y

    def setAndSolve(self, x):
        self.x = x
        self.y = x
        self.z = x

        return self.px(x), self.py(x), self.pz(x)

e = Equanimous()

# uniform distr of samples:
samples = n.arange(0, 100)

r = e.setAndSolve([i for i in samples])

# 3d plot of:
data = [e.px(samples), e.py(samples), e.pz(samples)]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(data[0], data[1], data[2])
plt.show()

