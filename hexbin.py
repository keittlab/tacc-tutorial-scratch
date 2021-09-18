import matplotlib as mpl
mpl.use('Agg') #use headless matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=50000)
y = (x * 3 + np.random.normal(size=50000)) * 5

plt.hexbin(x, y, gridsize=(25,25), cmap=plt.cm.Greens)
plt.savefig("hexbin.png")
