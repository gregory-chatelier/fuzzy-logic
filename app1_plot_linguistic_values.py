from matplotlib import pyplot as plt
from fuzzy_system import *


lfs = LeftFuzzySet(0, 35, 10, 12)
tfs1 = TrapezoidalFuzzySet(0, 35, 10, 12, 15, 17)
tfs2 = TrapezoidalFuzzySet(0, 35, 15, 17, 20, 25)
rfs = RightFuzzySet(0, 35, 20, 25)


# Plot 1 - Each linguistic value

fig, axs = plt.subplots(1, 4, figsize=(14, 2.2), sharey=True)

xs = [pt.x for pt in lfs.points]
ys = [pt.y for pt in lfs.points]
axs[0].plot(xs, ys, alpha=0.75, color='#539ecd', linestyle='solid')
axs[0].title.set_text("Froid")


xs = [pt.x for pt in tfs1.points]
ys = [pt.y for pt in tfs1.points]
axs[1].plot(xs, ys, alpha=0.75, color='#539ecd', linestyle='solid')
axs[1].title.set_text("Frais")


xs = [pt.x for pt in tfs2.points]
ys = [pt.y for pt in tfs2.points]
axs[2].plot(xs, ys, alpha=0.75, color='#539ecd', linestyle='solid')
axs[2].title.set_text("Bon")


xs = [pt.x for pt in rfs.points]
ys = [pt.y for pt in rfs.points]
axs[3].plot(xs, ys, alpha=0.75, color='#539ecd', linestyle='solid')
axs[3].title.set_text("Chaud")

plt.xlabel("Temperature")
plt.tight_layout()

plt.show()

