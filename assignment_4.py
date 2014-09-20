import pandas as pd
import numpy as np
print 

# pandas version 0.14.1


col_names = ['continent', 'status', 'order', 'family', 'genus', 'species', 
             'log_mass', 'combined_mass', 'reference']

data = pd.read_csv('MOMv3.3.txt', sep='\t', names = col_names)

#data = pd.read_csv('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt',
                     #sep='\t', names = col_names) #slower url reader.
                     
# Just playing with indexing
#print data['Log_mass'].iloc[12:17]  #This prints rows 12 - 16. i for index, 
#   first data row is zero.
#print data['Log_mass'][12:17]  #This does the same bloody thing
#print data['Log_mass'].loc[12:17]  #This prints rows 12 - 17
#print data.head(12)

#Now play with groupby and get some stats
#bystatus = data.groupby('status')
#print bystatus['combined_mass'].describe()# well that is fucking awesome

#Now get back to the homework:
#print len(data)# answer = 5731

#Q1.1
print "number of genera: ", len(data.groupby(['genus']))# answer = 1247

# Now see if you can count the number of unique species.
print "number of species: ", len(data.groupby(['genus', 'species']))# answer = 4889

#species_bystatus = data.groupby(['status', 'genus', 'species'])
#print species_bystatus['status'].count()


# Q1.2
extant = data[data['status'] == 'extant']
print "number of unique extant species: ", len(
                     extant.groupby(['genus', 'species']))

extinct = data[data['status'] == 'extinct']
print "number of unique extinct species: ", len(
                     extinct.groupby(['genus', 'species']))

#Q1.3
print "number of families: ", len(data.groupby(['family']))

#Q1.4

#first extract row of heaviest species
max_row = data[data['combined_mass'] == data['combined_mass'].max()]
# now print the three columns.
print "Here is the info for the largest species in the list:"
print max_row[['genus','species', 'combined_mass']]

#first extract row of smallest species
more_than_zero = data[data['combined_mass'] > 0.0]
min_row = more_than_zero[more_than_zero['combined_mass'] == more_than_zero[
                     'combined_mass'].min()]
# now print the three columns.
# asshole - need to loop through rows
print ""
print "Here is the info for the smallest species in the list:"
print min_row[['genus','species', 'combined_mass']]

# Q1.5
print ""
print "Q 1.5:"
y = extinct['combined_mass'].mean()
print "The average mass of extant species is %.2f grams and the average mass \
of extinct species is %.2f grams." % (extant['combined_mass'].mean(), 
                                      extinct['combined_mass'].mean())


#Q2
continents = data.groupby(['continent', 'status'])

continents_table = continents["continent", 'status', 'combined_mass'].mean()
print ""
#print continents_table

# now look up stuff:
#continents_table.loc['AF', 'extant']
#combined_mass    22208.229331
#Name: (AF, extant), dtype: float64

# Problem is that continents_table is just a list of means. Meanwhile, continent and status
# are only indices, not part of the data!  Need to reset the DataFrame index:

new_cont_table = continents_table.reset_index()
#print new_cont_table #That worked!



# Now for ugly string code to get desired output
cont = ''
mass_diff = open('continent_mass_differences.csv', 'w')
header = 'continent' + ',' + 'extant_mean' + ',' 'extinct_mean' + ',' + 'difference' + ',' + 'ratio' + '\n'
mass_diff.write(header)
newline = ''
for line in new_cont_table.values:
    if line[0] != cont:# starting new row = new continent
        cont = line[0]
    if line[1] == 'extant':
        extant_mean = round((line[2]),2)
        newline = cont + ',' + str(extant_mean)
    elif line[1] == 'extinct':
        extinct_mean = round((line[2]),2)
        diff = abs(extant_mean - extinct_mean)
        ratio = extinct_mean/extant_mean
        newline += ',' + str(extinct_mean) + ',' + str(diff) + ',' + str(ratio) + '\n'
        mass_diff.write(newline)
        newline = ''
                
mass_diff.close()