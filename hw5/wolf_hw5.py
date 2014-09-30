import pandas as pd
import numpy as np
import itertools as it

data = pd.read_csv('TGPP_pres.csv')

#print len(data["plot"].unique())# 20 plots
#print len(data["year"].unique())#1999 - 2009. no missing. 12 years
#print len(data["scale"].unique()) # 5 scales
#print len(data["spcode"].unique())# 320 species
#print len(data)
paulslist = ['A', 'B', '76', 'G', '66']

g = it.combinations(paulslist, 2)

for i in g:
	print i


#data_array = np.array(data)
#print len(data)
 

