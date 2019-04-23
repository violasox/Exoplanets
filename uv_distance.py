import numpy as np
import matplotlib
from matplotlib import pyplot
import pickle
from find_overlap import Exoplanet
import math

matplotlib.rcParams.update({'font.size': 18})

with open('project.dat', 'rb') as f:
    foundExoplanets = pickle.load(f)

dist = []
uvMag = []
for exoplanet in foundExoplanets:
    if exoplanet.uv[3] is not None and exoplanet.dist is not None:
        mag = -2.5*math.log10(exoplanet.uv[3]) - 21.175
        uvMag.append(mag)
        dist.append(exoplanet.dist)

fit = np.polyfit(dist, uvMag, 1)
distRange = np.linspace(0, 175, 10)
fitFunc = np.poly1d(fit)
pyplot.plot(dist, uvMag, 'bo', alpha=0.5)
pyplot.plot(distRange, fitFunc(distRange), 'k', linewidth=3)
pyplot.xlabel('Distance to host star [pc]')
pyplot.ylabel('UV Absolute Visual Magnitude')
pyplot.tight_layout()
pyplot.savefig('figures/uv_vs_distance.pdf')
pyplot.show()
