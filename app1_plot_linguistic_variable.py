from matplotlib import pyplot as plt
from fuzzy_system import *


# Plot 2 - Linguistic variable

lfs = LeftFuzzySet(0, 35, 10, 12)
tfs1 = TrapezoidalFuzzySet(0, 35, 10, 12, 15, 17)
tfs2 = TrapezoidalFuzzySet(0, 35, 15, 17, 20, 25)
rfs = RightFuzzySet(0, 35, 20, 25)


xs = [pt.x for pt in lfs.points]
ys = [pt.y for pt in lfs.points]

plt.plot(xs, ys, alpha=0.75, color='#663FB6', linestyle='solid')
plt.fill_between(xs, ys, alpha=0.25, color='#663FB6')

xs = [pt.x for pt in tfs1.points]
ys = [pt.y for pt in tfs1.points]

plt.plot(xs, ys, alpha=0.75, color='#539ECD', linestyle='solid')
plt.fill_between(xs, ys, alpha=0.25, color='#539ECD')

xs = [pt.x for pt in tfs2.points]
ys = [pt.y for pt in tfs2.points]

plt.plot(xs, ys, alpha=0.75, color='#FEBD2D', linestyle='solid')
plt.fill_between(xs, ys, alpha=0.25, color='#FEBD2D')

xs = [pt.x for pt in rfs.points]
ys = [pt.y for pt in rfs.points]

plt.plot(xs, ys, alpha=0.75, color='#DF2318', linestyle='solid')
plt.fill_between(xs, ys, alpha=0.25, color='#DF2318')


plt.xlabel("Temperature")

plt.show()
