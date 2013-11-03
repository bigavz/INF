import numpy as np
import pylab as py

raster = [0]
i=0
while i<5:
    raster.append(i*np.exp(0-i))
    i+=1


py.plot(range(0,len(raster),1), np.transpose(raster), 'b.')
py.show()

print(raster)