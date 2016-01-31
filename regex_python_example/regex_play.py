import re
 
inputfile = open('rodents.txt', 'rU')
 
def get_species(inputstring):
    species_re = "([A-Z][a-z]+ [a-z]+)"
    species_search = re.search(species_re, inputstring)
    if species_search:
        return species_search.group(1)
    
 
results = []
nomatch = []
for line in inputfile:
    species = get_species(line)
    if species:
        results.append(species)
    else:
        nomatch.append(line)
				
	

