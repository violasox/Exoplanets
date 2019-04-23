import numpy as np
import matplotlib
from matplotlib import pyplot
import pickle
from find_overlap import Exoplanet
import math

matplotlib.rcParams.update({'font.size': 18})

with open('project.dat', 'rb') as f:
    foundExoplanets = pickle.load(f)

axis = []
flux = []
cFlux = []
for exoplanet in foundExoplanets:
    if (exoplanet.uv[2] is not None and exoplanet.uv[3] is not None and 
        exoplanet.dist is not None and exoplanet.axis is not None):
        avgFluxEarth = (exoplanet.uv[3] + exoplanet.uv[2]) / 2
        exoDistAu = exoplanet.dist*(648000/math.pi)
        avgFluxExo = avgFluxEarth*((exoDistAu**2)/(exoplanet.axis**2))
        # mW to W and A-1 to over 2000A range (2000-4000)
        avgFluxExo *= (2000/1000)
        # 800A range (2000-2800)
        uvcFluxExo = avgFluxExo * (800/2000)
        flux.append(avgFluxExo)
        cFlux.append(uvcFluxExo)
        axis.append(exoplanet.axis)

flux = np.array(flux)
cFlux = np.array(cFlux)
axis = np.array(axis)
# goodFluxIndices = np.where(flux < 89.90)[0]
# print(len(goodFluxIndices))
# badFluxIndices = np.where(flux >= 89.90)[0]
# print(len(badFluxIndices))
# pyplot.loglog(axis[goodFluxIndices], flux[goodFluxIndices], 'go', alpha=0.5)
# pyplot.loglog(axis[badFluxIndices], flux[badFluxIndices], 'ro', alpha=0.5)
# pyplot.xlabel('Semi-Major Axis [Au]')
# pyplot.ylabel('UV flux at Exoplanet [$W \cdot m^-2$]')
# pyplot.axhline(89.90, color='k')
# pyplot.legend(['Good flux', 'Bad flux', '89.9$W m^-2$'], loc='lower left')
# pyplot.tight_layout()
# pyplot.savefig('figures/flux_vs_axis.pdf')
# 
# goodFluxIndices = np.where(flux < 10e-23)[0]
# badFluxIndices = np.where(flux >= 10e-23)[0]
# pyplot.loglog(axis[goodFluxIndices], cFlux[goodFluxIndices], 'go', alpha=0.5)
# pyplot.loglog(axis[badFluxIndices], cFlux[badFluxIndices], 'ro', alpha=0.5)
# pyplot.xlabel('Semi-Major Axis [Au]')
# pyplot.ylabel('UV flux at Exoplanet [$W \cdot m^-2$]')
# pyplot.axhline(10e-23, color='k')
# pyplot.legend(['Good flux', 'Bad flux', '$10^-23W m^-2$'], loc='center left')
# pyplot.tight_layout()
# pyplot.savefig('figures/cflux_vs_axis.pdf')

goodFluxIndices = (flux < 89.9) & (axis > 0.95) & (axis < 2.4)
print(len(axis[goodFluxIndices]))
badFluxIndices = ~goodFluxIndices
pyplot.loglog(axis[goodFluxIndices], flux[goodFluxIndices], 'go', alpha=1)
pyplot.loglog(axis[badFluxIndices], flux[badFluxIndices], 'ro', alpha=0.5)
pyplot.xlabel('Semi-Major Axis [Au]')
pyplot.ylabel('UV flux at Exoplanet [$W \cdot m^-2$]')
pyplot.axhline(89.90, color='k')
pyplot.axvspan(0.85, 2.4, alpha=0.3, color='k')
pyplot.tight_layout()
pyplot.savefig('figures/habitable_zone.pdf')
pyplot.show()
