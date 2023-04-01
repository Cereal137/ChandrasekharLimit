#%%
import numpy as np
import matplotlib.pyplot as plt
#define a datatype with two float
MRtype = np.dtype({
    'names':['rho', 'R','M'],
    'formats':['f','f', 'f']})

#load the data
D = np.loadtxt('M-R.txt',dtype=MRtype)
#plot the data
plt.plot(np.log(D['rho'])/np.log(10),D['M'])
plt.ylabel('M/M_solar')
plt.xlabel('$lg[ρ_c/(1\mathrm{g/cm^3})]$')
#plt.xlim(0,17000)
plt.ylim(0,1.5)
plt.title('the Mass-Density relation')
plt.savefig('ChandrasekharLimit_Mass-Density.jpg',dpi=400)
plt.show()
# %%
