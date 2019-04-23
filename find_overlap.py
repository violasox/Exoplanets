from astropy.io import ascii
from astropy.io import fits
from astropy.table import Table
import string
import numpy as np
import pickle

class Exoplanet():
    def __init__(self):
        self.uv = None
        self.dist = None
        self.mass = None
        self.radius = None
        self.axis = None


if __name__ == '__main__':
    exoplanets = ascii.read('exoplanets.csv')
    stars = fits.open('TD1.fits')
    stars = Table(stars[1].data)

    print(exoplanets.info())
    # print(stars.info())
    starDict = {}
    for i, starNum in enumerate(stars['HD_NUMBER']):
        starDict[str(starNum)] = i

    overlapCount = 0
    indices = np.where(~np.ma.getmask(exoplanets['star_name']))[0]
    altIndices = np.where(~np.ma.getmask(exoplanets['star_alternate_names']))[0]
    foundExoplanets = []
    for index in indices:
        starNames = []
        starNames.append(str(exoplanets[index]['star_name']))
        if index in altIndices:
            newNames = exoplanets['star_alternate_names'][index].split(', ')
            starNames += newNames
        for name in starNames:
            if name.startswith('HD'):
                starNum = str(name.replace('HD ', ''))
                if starNum in starDict:
                    starIndex = starDict[starNum]
                    overlapCount += 1
                    e = Exoplanet()
                    star = stars[starIndex]
                    e.uv = [star['FLUX_1565_A'], star['FLUX_1965_A'], star['FLUX_2365_A'], 
                            star['FLUX_2740_A']]
                    dist = exoplanets[index]['star_distance']
                    mass = exoplanets[index]['mass']
                    radius = exoplanets[index]['radius']
                    axis = exoplanets[index]['semi_major_axis']
                    if not np.ma.is_masked(dist):
                        e.dist = dist
                    if not np.ma.is_masked(mass):
                        e.mass = mass
                    if not np.ma.is_masked(radius):
                        e.radius = radius
                    if not np.ma.is_masked(axis):
                        e.axis = axis
                    foundExoplanets.append(e)
    with open ('project.dat', 'wb') as f:
        pickle.dump(foundExoplanets, f, pickle.HIGHEST_PROTOCOL)
    print(overlapCount)
