import numpy as n
import matplotlib.pyplot as plt

def boxVolume(length):
    return length ** 3

# Assumption:
# it is a natural law that the total volume of boxes is distributed uniformly in this sense:
# if a box has more volume, less often it occurs, but the total volume allocated to a box size is constant:
# sizes = n.arange(1, 6, 0.1)  # uniform distribution OR
# sizes = n.random.uniform(1, 6, 100)  # uniform distribution
# samples hold size samples to make our boxes, lets say the length of edge of a square box

# plt.plot(samples, p(b), 'ro' if lin else '-')
# plt.show()

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
    v = boxVolume(sizes)
    p_ = p(v)
    if log:
        v = n.log(v)
        p_ = n.log(p_)
    plt.plot(v, p_, '-' if lin else 'ro')
    plt.show()
