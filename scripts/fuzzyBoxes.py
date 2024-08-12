import numpy as n
import matplotlib.pyplot as plt

def boxVolume(x, y, z=None):
    # z = y ** 0.5
    z = z + y
    return x * y * z

def p(boxvolume):  # probability 1 / xˆ3, alpha = 3
    return 1 / boxvolume

def plotBoxesProbabilities(lin=True, log=False):
    '''
    the density on the tail is greater,
    but those are not boxes, those of probabilities of box sizes.
    The higher density is because the probability varies more slowly with the size of the box, so there are more box sizes in a small area.
    Each point is the probability of a box size, not the box size itself.
    '''
    if lin:
        sizes = n.arange(1, 6, 0.1)  # uniform distribution
    else:
        sizes = n.random.uniform(1, 6, 100)  # uniform distribution
    v = boxVolume(sizes, sizes, sizes)
    p_ = p(v)
    if log:
        v = n.log(v)
        p_ = n.log(p_)
    plt.plot(v, p_, '-' if lin else 'ro')
    plt.show()

