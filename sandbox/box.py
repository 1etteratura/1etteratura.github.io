import numpy as n
import matplotlib.pyplot as plt

__doc__ = '''
This file defines box types (classes) and plots their probabilities.

The basic box has alpha = 3, and the fuzzy box has alpha = ?


'''

class BasicBox:
    '''
    v = r**3
    '''
    def __init__(self, seq=True, log=False, show=True, default=True, xtype='volume'):
        self.calcDistr(seq)  # defines self.seq here, used by plot
        self.x = self.vs
        self.calcAlpha()

        self.seq = seq
        self.log = log
        self.show = show
        self.xtype = xtype
        print('init ok')
        if default:
            print('entering default')
            self.default()

    def setParameters(self, r):
        self.r = r

    def calcVolume(self):
        self.volume = self.r ** 3

    def calcProb(self):
        self.prob = 1 / self.volume

    def calcDistr(self, seq=True):
        # uniform distribution
        self.seq = seq
        if seq:
            sizes = n.arange(1, 6, 0.1)  # sequential
        else:
            sizes = n.random.uniform(1, 6, 100)  # in random order
        vs = []
        ps = []
        for s in sizes:
            self.setParameters(s)
            self.calcVolume()
            self.calcProb()
            ps.append(self.prob)
            vs.append(self.volume)
        self.vs = vs
        self.ps = ps
        self.sizes = sizes

    def mkLog(self):
        self.vs_log = n.log(self.vs)
        self.ps_log = n.log(self.ps)
        self.x_log = n.log(self.x)
        self.sizes_log = n.log(self.sizes)

    def calcAlpha(self):
        self.mkLog()
        m, b = n.polyfit(self.x_log, self.ps_log, 1)
        self.alpha = m
        self.b = b
        print(self.alpha, self.b)

    def plot(self, log=False, show=True, xtype='volume'):
        '''
        the density on the tail is greater,
        but those are not boxes, those of probabilities of box sizes.
        The higher density is because the probability varies more slowly with the size of the box, so there are more box sizes in a small area.
        Each point is the probability of a box size, not the box size itself.
        '''
        self.mkLog()
        self.setX(xtype)
        stroke = '-' if self.seq else 'o'
        if log:
            x = self.x_log
            y = self.ps_log
        else:
            x = self.x
            y = self.ps
        plt.plot(x, y, stroke)
        print(show, 'mann')
        if show:
            plt.title(f'a = {self.alpha:10.4f}, b = {self.b:10.4f}')
            plt.show()

    def default(self):
        print('inside default')
        self.plot(True, False)
        self.calcDistr(False)
        print('executed one plot')
        self.plot(True, True)

    def setX(self, xtype='volume'):
        self.xtype = xtype
        if xtype == 'volume':
            self.x = self.vs
            self.x_log = self.vs_log
        else:
            self.x = self.sizes
            self.x_log = self.sizes_log



class BasicBox2(BasicBox):
    def __init__(self, xtype='volume'):
        BasicBox.__init__(self, xtype=xtype)
        self.setX(xtype)

    def calcVolume(self):
        x = self.r
        y = 2 * self.r ** 0.3
        z = 0.2 * self.r
        self.volume = x * y * z

    def default(self):
        print('inside default 2')
        self.plot(True, False)
        self.calcDistr(False)
        print('executed one plot')
        self.plot(True, True)


class FuzzyBox(BasicBox):
    '''
    e.g.:
    v = x * y * (z + 2y)
    '''
    def __init__(self, x=1, y=1, z=1):
        self.setBox(x, y, z)
        self.calcVolume()
        self.calcProb()

    def setBox(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calcVolume(self):
        self.volume = self.x * self.y * (self.z + 2 * self.y)

    def calcProb(self):
        self.prob = 1 / self.volume


    def plot(self, seq=True, log=False, show=True):
        if seq:
            sizes = n.arange(1, 6, 0.1)  # uniform distribution
        else:
            sizes = n.random.uniform(1, 6, 100)  # uniform distribution
        vs = []
        ps = []
        for s in sizes:
            self.r = s
            self.setBox(s, s, s)
            self.calcVolume()
            self.calcProb()
            self.calcVolume()
            ps.append(self.prob)
            vs.append(self.volume)
        if log:
            # sizes = n.log(sizes)
            vs = n.log(vs)
            ps = n.log(ps)
            m, b = n.polyfit(vs, ps, 1)
            print(m, b)
        plt.plot(vs, ps, '-' if seq else 'o')
        self.vs = vs
        self.ps = ps
        self.sizes = sizes
        if show:
            plt.show()


class ComplexBox(BasicBox):
    def __init__(self, seq=True, log=False, show=True, default=True):
        self.calcDistr(seq)
        self.seq = seq
        self.log = log
        self.show = show

        self.x = self.vs
        self.x_log = self.vs_log

        self.calcAlpha()

        if default:
            self.default()

    def setParameters(self, x, y, z):
        self.x = x
        # self.y = y + 2 * x ** 2
        self.y = 2 * x ** 2
        self.z = 3 * x

    def calcVolume(self):
        self.volume = self.x * self.y * self.z

    def calcDistr(self, seq=True, xtype='volume'):
        # uniform distribution
        self.seq = seq
        if seq:
            x = n.arange(1, 6, 0.1)  # sequential
            y = n.arange(1, 6, 0.1)  # sequential
            z = n.arange(1, 6, 0.1)  # sequential
        else:
            x = n.random.uniform(1, 6, 100)  # in random order
            y = n.random.uniform(1, 6, 100)  # in random order
            z = n.random.uniform(1, 6, 100)  # in random order
        vs = []
        ps = []
        for i in range(len(x)):
            self.setParameters(x[i], y[i], z[i])
            self.calcVolume()
            self.calcProb()
            ps.append(self.prob)
            vs.append(self.volume)
        self.sizes = dict(x=x, y=y, z=z)
        self.vs = vs
        self.ps = ps
        self.setX(xtype)

    def setX(self, xtype='volume'):
        self.xtype = xtype
        if xtype == 'volume':
            self.x = self.vs
        if sizes:
            self.x = self.sizes



if __name__ == '__main__':
    print('ok')
    # b = BasicBox()
    b2 = BasicBox2('size')
    # f = FuzzyBox()
    # c = ComplexBox()
