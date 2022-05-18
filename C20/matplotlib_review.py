import matplotlib.pyplot as plt

x = [0, 3, 6, 9, 14]
y = [0, 5, 2, 8, 10]

fig, axes = plt.subplots(nrows=1, ncols=3)

axes[0].scatter(x, y)
axes[1].plot(x, y)
axes[2].plot(x, y, 'o-')
plt.show()