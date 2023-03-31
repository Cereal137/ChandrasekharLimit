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
plt.plot(D['R'],D['M'])
plt.ylabel('M/M_solar')
plt.xlabel('R(km)')
plt.xlim(0,17000)
plt.ylim(0,1.5)
plt.title('the Mass-Radius relation')
plt.savefig('ChandrasekharLimit.jpg',dpi=400)
plt.show()

# %%
