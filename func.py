import numpy as np
def logNFW(r,rho0,Rs):
    return np.log10(rho0)-(np.log10(r/Rs)+2*np.log10(1+r/Rs))