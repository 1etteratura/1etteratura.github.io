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
    def __init__(self):
        self.calcDistr()
        self.calcAlpha()
        self.plot()

    def calcVolume(self):
        self.volume = self.r ** 3

    def calcProb(self):
        self.prob = 1 / self.volume

    def plotInitial(self, seq=True, log=False, show=True):
        '''
        the density on the tail is greater,
        but those are not boxes, those of probabilities of box sizes.
        The higher density is because the probability varies more slowly with the size of the box, so there are more box sizes in a small area.
        Each point is the probability of a box size, not the box size itself.
        '''
        if seq:
            sizes = n.arange(1, 6, 0.1)  # uniform distribution
        else:
            sizes = n.random.uniform(1, 6, 100)  # uniform distribution
        vs = []
        ps = []
        for s in sizes:
            self.r = s
            self.calcVolume()
            self.calcProb()
            self.calcVolume()
            ps.append(self.prob)
            vs.append(self.volume)
        if log:
            sizes = n.log(sizes)
            ps = n.log(ps)
            m, b = n.polyfit(volume, ps, 1)
            print(m, b)
        plt.plot(vs, ps, '-' if seq else 'o')
        self.vs = vs
        self.ps = ps
        self.sizes = sizes
        if show:
            plt.show()

    def calcDistr(self, seq=True):
        if seq:
            sizes = n.arange(1, 6, 0.1)  # uniform distribution
        else:
            sizes = n.random.uniform(1, 6, 100)  # uniform distribution
        vs = []
        ps = []
        for s in sizes:
            self.r = s
            self.calcVolume()
            self.calcProb()
            self.calcVolume()
            ps.append(self.prob)
            vs.append(self.volume)
        self.vs = vs
        self.ps = ps
        self.sizes = sizes

    def mkLog(self):
        self.vs_ = n.log(self.vs)
        self.ps_ = n.log(self.ps)

    def calcAlpha(self):
        self.mkLog()
        m, b = n.polyfit(self.vs_, self.ps_, 1)
        self.alpha = m
        self.b = b
        print(self.alpha, self.b)

    def plot(self, seq=True, log=False, show=True):
        if log:
            self.mkLog()
            plt.plot(self.vs_, self.ps_, '-' if seq else 'o')
            return
        plt.plot(self.vs, self.ps, '-' if seq else 'o')
        if show:
            plt.show()


    def default(self):
        self.plot()

        self.plot(False)

        self.plot(True, True)

        self.plot(True, True, False)
        self.plot(False, True, True)


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


if __name__ == '__main__':
    print('ok')
    b = BasicBox()
    f = FuzzyBox()
