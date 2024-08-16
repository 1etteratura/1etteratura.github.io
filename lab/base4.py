import numpy as n
import matplotlib.pyplot as plt

def C(a, kl, kr):
    if a = 1:
        return - 1 / (kr - kl)
    f = 1 - a
    return f / (kr ** f - kl ** f)

def p(c, a, k):
    return c * k ** (-a)

def p_(a, kl, kr, k):
    return C(a, kl, kr) * k ** (-a)

class PowerLaw:
    def __init__(self, a, kl, kr):
        self.a = a
        self.kl = kl
        self.kr = kr

    def p(self, k):
        return p_(self.a, self.kl, self.kr, k)

    def __str__(self):
        return "StandardPowerLaw(a=%s, kl=%s, kr=%s)" % (self.a, self.kl, self.kr)


class StandardPowerLaw(PowerLaw):
    def __init__(self, a):
        PowerLaw.__init__(self, a, 0, 1)

    def __str__(self):
        return "StandardPowerLaw(a=%s)" % self.a

class CanonicPowerLaw(PowerLaw):
    def __init__(self):
        PowerLaw.__init__(self, c=1, k1=0, kr=1)

    def __str__(self):
        return "StandardPowerLaw(a=%s)" % self.a

# fix kl and kr, plot c while a varies
kl = 1
kr = 100
a = n.linspace(0.95, 1.05, 1000000)
# a[10] = 1
c = C(a, kl, kr)
plt.plot(a, c)
plt.show()
# result: c grows as a grows

# problem to calculate c when a = 1
c(1, kl, kr)  # error
# zero in both denominator and nominator
