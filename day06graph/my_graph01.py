import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot([0, 0, 0], [0, 2, 4], [0, 5, 0], '')
#ax.plot([x1, x2, x3], [y1, y2, y3], [z1, z2, z3], '')

plt.show()