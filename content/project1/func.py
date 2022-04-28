import numpy as np
from scipy.constants import pi



def GDP(r,rho0,Rs,alpha,beta,gamma):
    return rho0/((r/Rs)**gamma * (1+(r/Rs)**alpha)**((beta-gamma)/alpha))



def NFW(r,rho0,Rs):
    return rho0/((r/Rs)*(1+r/Rs)**2)



def distance(c0,x0,c1,x1,c2,x2):
    return np.sqrt((abs(c0-x0)**2)+(abs(c1-x1)**2)+(abs(c2-x2)**2))



def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    if bool(idx)=='False':
       idx=1
    return idx



def dens_prof(Rbin,Rins,galdist,mp):
    prof=[],[]
    Rmax=np.amax(galdist)
    for n in range(2,100):
        n=n/100
        R1=Rins
        if (R1>Rmax):
            break
        R2=n*Rbin
        Npart=0
        for i in range(len(galdist)):       
            if (galdist[i]>R1 and galdist[i]<R2):
                Npart+=1
        dens=Npart*mp/(1.25*pi*(R2**3-R1**3))
        if dens==0:
            dens=1
        prof[0].append(R1)
        prof[1].append(dens)
        Rins=R2
    pos=[]
    for i in range(len(prof[1])):
        if prof[1][i]==1:
            pos.append(i)

    dens=np.delete(prof[1],pos)
    r=np.delete(prof[0],pos)
    return r,dens

    
    