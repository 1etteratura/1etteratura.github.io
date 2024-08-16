import numpy as n
import matplotlib.pyplot as plt

BOX = 100  # size of side of bigger box
V = BOX ** 3  # volume of bigger box
ls = n.arange(1, 10)
vs = ls ** 3
c = 'bo-'

# case 1, boxes dont superpose:
counts = V / vs
fig, axs = plt.subplots(2)
fig.suptitle('case 1: boxes dont superpose/compete')
axs[0].plot(ls, counts, c)
axs[0].set_title('counts x side length')
axs[1].plot(n.log(ls), n.log(counts), c)
axs[1].set_title('log(counts) x log(side length)')
plt.savefig('box_case1.png')
plt.show()

# case 2, boxes superpose, fills portion of volume, but first the smaller boxes are input:

f = 0.4  # that is, boxes tend to occupy 0.3 of the empty space
V_ = V  # empty space
counts = []
for l in ls:
    Vv = V_ * f  # space to be occupied
    v = l ** 3
    count = Vv / v
    counts.append(count)
    V_ = V_ - v * count  # remaining space

fig, axs = plt.subplots(2)
fig.suptitle('case 2: boxes superpose/compete, small boxes placed first')
axs[0].plot(ls, counts, c)
axs[0].set_title('counts x side length')
axs[1].plot(n.log(ls), n.log(counts), c)
axs[1].set_title('log(counts) x log(side length)')
plt.savefig('box_case2.png')
plt.show()

# third case, boxes superpose, fills portion of volume, but first the bigger boxes are input:


V_ = V  # empty space
counts = []
for v in vs[::-1]:
    Vv = V_ * f  # space to be occupied
    count = Vv / v
    counts.append(count)
    V_ = V_ - v * count  # remaining space

counts = counts[::-1]

fig, axs = plt.subplots(2)
fig.suptitle('case 3: boxes superpose/compete, big boxes placed first')
axs[0].plot(ls, counts, c)
axs[0].set_title('counts x side length')
axs[1].plot(n.log(ls), n.log(counts), c)
axs[1].set_title('log(counts) x log(side length)')
plt.savefig('box_case3.png')
plt.show()
