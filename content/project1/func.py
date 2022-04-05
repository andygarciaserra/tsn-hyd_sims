import numpy as np

def logNFW(r,rho0,Rs):
    return np.log10(rho0)-(np.log10(r/Rs)+2*np.log10(1+r/Rs))

def NFW(r,rho0,Rs):
    return rho0/((r/Rs)*(1+r/Rs)**2)

def distance(c0,x0,c1,x1,c2,x2):
    return np.sqrt((abs(c0-x0)**2)+(abs(c1-x1)**2)+(abs(c2-x2)**2))
