#Packages:
import h5py
import os
import numpy as np    
import matplotlib.pyplot as plt
from scipy.constants import pi
from scipy.optimize import curve_fit as fit
import func as func
import random
from tqdm import tqdm

#Cálculo de histogramas simulados:
datadir = "G2-lcdm-gas/"
files = os.listdir(datadir+".")
files.sort()

f = h5py.File(datadir+"snapshot_004.hdf5", "r")
group = f["PartType0"]
data = group["Coordinates"][()]
dmax=np.sqrt(3)*50000

hist=[]
hist=np.array(hist)

part=30000     #Number of particles to loop distances:

for j in tqdm(range(part)):
    d=[]
    for i in range(1,len(data)):
        r=func.distance(data[j,0],data[i,0],data[j,1],data[i,1],data[j,2],data[i,2])
        d=np.append(d,r)
    output=np.histogram(d,bins=100,range=(0,dmax))
    counts=output[0]
    n=np.array(counts)
    hist=np.concatenate((hist,counts),axis=0) 
hist=np.split(hist,part)
np.savetxt("hist.txt", hist, delimiter =", ")



# Random disposition:
    #Number of particles involved in randomization:
n = 32700

    #Setting limits for each coordinate:
x1, x2 = 0, 50000
y1, y2 = 0, 50000
z1, z2 = 0, 50000

    #Defining the final coordinate vectors randomly:
x = (x2 - x1)*np.random.rand(n) + x1
y = (y2 - y1)*np.random.rand(n) + y1
z = (z2 - z1)*np.random.rand(n) + z1

    #Same measuring block as before, histogram making looping each particle:
dmax=np.sqrt(3)*50000
histrand=[]
histrand=np.array(histrand)
 
for j in tqdm(range(part)):
    d=[]
    for i in range(1,len(x)):
        r=func.distance(x[j],x[i],y[j],y[i],z[j],z[i])
        d=np.append(d,r)
    output=np.histogram(d,bins=100,range=(0,dmax))
    counts=output[0]
    n=np.array(counts)
    histrand=np.concatenate((histrand,counts),axis=0)
histrand=np.split(histrand,part)
np.savetxt("histrand.txt", histrand, delimiter =", ")


#Ploteo final de histogramas:
histogram=np.average(hist,axis=0)
histogramrand=np.average(histrand,axis=0)
plt.plot(histogram)
plt.plot(histogramrand)
plt.savefig('histogramas-finales.png')



