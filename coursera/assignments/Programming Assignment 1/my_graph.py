import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import spline
import pandas as pd

# Preparing dataset and variables
dataset = pd.read_csv('ExcelFormattedGISTEMPData2CSV.csv')
x = dataset.iloc[:, 0].values           # Years
yTempGlob = dataset.iloc[:, 1].values   # Global temperatures
yTempNHem = dataset.iloc[:, 2].values   # North Hemispheres temperatures
yTempSHem = dataset.iloc[:, 3].values   # South Hemispheres temperatures

# # Inspect variables
# print(x)
# print(yTempGlob)
# print(yTempNHem)
# print(yTempSHem)

# Scale x and y axis scale
xdist = x.max() - x.min()
xscale = (xdist // 10) * 10 + 10
ymin = min([yTempGlob.min(), yTempNHem.min(), yTempSHem.min()])
ymax = max([yTempGlob.max(), yTempNHem.max(), yTempSHem.max()])
yscale = max([ymax, abs(ymin)])
yscale = (yscale // 10) * 10 + 10

# Alright, all are goods.
# Lets preparing for plotting
# mpl.style.use('classic')
fig = plt.figure()
fig.suptitle(
    'GISTEMP data for the Globe and the North and South Hemispheres From 1880 to 2014\n',
    fontsize=14,
    ha='center')
ax = fig.add_subplot(1, 1, 1)

# Plot x-y lines
xIndexes = np.arange(xdist+1)
xSmooth = np.linspace(0, xdist, xdist*3+3)
yTempGlobSmooth = spline(xIndexes, yTempGlob, xSmooth)
yTempNHemSmooth = spline(xIndexes, yTempNHem, xSmooth)
yTempSHemSmooth = spline(xIndexes, yTempSHem, xSmooth)
ax.plot(xSmooth, yTempGlobSmooth, linestyle='-', linewidth=1, color='#389986', marker='*', label='Global', markevery=30)
ax.plot(xSmooth, yTempNHemSmooth, linestyle='-', linewidth=1, color='#ffa733', marker='o', label='North Hemispheres', markevery=30)
ax.plot(xSmooth, yTempSHemSmooth, linestyle='-', linewidth=1, color='#ff4133', marker='s', label='South Hemispheres', markevery=30)
ax.legend(loc='best')

ax.set_xlim((-5, xscale))
ax.set_xticklabels([1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000])
ax.set_xlabel('Year')
# ax.set_ylim((ymin-10, ymax+10))
# ax.set_yticks(range(-yscale, yscale, 20))
ax.set_ylabel('Temperature')
ax.grid(True)
ax.spines["right"].set_visible(False)     # Remove right axis
ax.spines["top"].set_visible(False)       # Remove top axis

plt.show()