from astropy.io import ascii
from astropy.io import fits
from astropy.table import Table
import string
import numpy as np

exoplanets = ascii.read('exoplanets.csv')
stars = fits.open('TD1.fits')
stars = Table(stars[1].data)

print(exoplanets.info())
print(stars.info())
starDict = {}
for i, starNum in enumerate(stars['HD_NUMBER']):
    starDict[str(starNum)] = i

overlapCount = 0
indices = ~np.ma.getmask(exoplanets['star_name'])
for hostStarName in exoplanets['star_name'][indices]:
    print(hostStarName)
    if hostStarName.startswith('HD'):
        starNum = str(hostStarName.replace('HD ', ''))
        if starNum in starDict:
            overlapCount += 1

print(overlapCount)
