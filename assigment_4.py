import pandas as pd
# pandas version 0.14.1


col_names = ['Continent', 'Status', 'Order', 'Family', 'Genus', 'Species', 
             'Log_mass', 'Combined_mass', 'Reference']

data = pd.read_csv('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt',
                     sep='\t', names = col_names)
#print data.head()


species_numb = data.groupby(['Continent'].unique())
print species_numb.head()



         


