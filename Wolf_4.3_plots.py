import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

col_names = ['continent', 'status', 'order', 'family', 'genus', 'species', 
             'log_mass', 'combined_mass', 'reference']

data = pd.read_csv('MOMv3.3.txt', keep_default_na = False, sep='\t', names = col_names)
data = data[data['combined_mass'] > 0.0]

extant = data[data['status'] == 'extant']
extinct = data[data['status'] == 'extinct']
extant_masses = np.array(extant['log_mass'])
extinct_masses = np.array(extinct['log_mass'])
all_masses = data['log_mass']#why does this work, but above does not unless convert to np.array


#plt.hist(all_masses, 20)
         
plt.hist(extinct_masses, 20, alpha=0.5)
plt.hist(extant_masses, 20, alpha=0.3)

#plt.savefig('savefigexample.eps', format='eps', dpi=1000)
plt.show()