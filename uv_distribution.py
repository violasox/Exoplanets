import numpy as np
import matplotlib
from matplotlib import pyplot
import pickle
from find_overlap import Exoplanet

matplotlib.rcParams.update({'font.size': 18})

with open('project.dat', 'rb') as f:
    foundExoplanets = pickle.load(f)

uvBand = []
uvMag = []
for exoplanet in foundExoplanets:
    uvBand += [0, 1, 2, 3]
    uvMag += exoplanet.uv

pyplot.semilogy(uvBand, uvMag, 'bo', alpha=0.5)
pyplot.ylabel('UV Flux [$mW m^{-2} A^{-1}$]')
pyplot.xticks([0,1,2,3], [1565,1965,2365,2740])
pyplot.xlabel('UV band [A]')
pyplot.title('UV flux of stars with known exoplanets')
pyplot.tight_layout()
pyplot.savefig('figures/uv_distribution.pdf')
pyplot.show()
