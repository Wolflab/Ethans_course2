import pandas as pd
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

#Q4.1
print "number of genera: ", len(data.groupby(['genus']))# answer = 1247

# Now see if you can count the number of unique species.
print "number of species: ", len(data.groupby(['genus', 'species']))# answer = 4889

#species_bystatus = data.groupby(['status', 'genus', 'species'])
#print species_bystatus['status'].count()


# Q4.2
extant = data[data['status'] == 'extant']
print "number of unique extant species: ", len(
                     extant.groupby(['genus', 'species']))

extinct = data[data['status'] == 'extinct']
print "number of unique extinct species: ", len(
                     extinct.groupby(['genus', 'species']))

#Q4.3
print "number of families: ", len(data.groupby(['family']))

#Q4.4

#first extract row of heaviest species
max_row = data[data['combined_mass'] == data['combined_mass'].max()]
# now print the three columns.
print "Here is the info for the largest species in the list:"
print max_row[['genus','species', 'combined_mass']].set_index(['genus'])

#first extract row of smallest species
more_than_zero = data[data['combined_mass'] > 0.0]
min_row = more_than_zero[more_than_zero['combined_mass'] == more_than_zero[
                     'combined_mass'].min()]
# now print the three columns.
# asshole - need to loop through rows
print ""
print "Here is the info for the smallest species in the list:"
print min_row[['genus','species', 'combined_mass']].set_index(['genus'])

# Q4.5
print ""
print "Q 4.5:"
y = extinct['combined_mass'].mean()
print "The average mass of extant species is %.2f grams and the average mass of extinct species is %.2f grams." % (extant['combined_mass'].mean(), extinct['combined_mass'].mean())