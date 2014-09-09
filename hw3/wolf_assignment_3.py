

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
        ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
        ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
        ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
        ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
        ['D5', 98], ['D6', 32]]

# 1. How many sites are there?
print "number of sites: ", len(data), '\n'

# 2. How many birds were counted at the 7th site?
print "# birds at 7th site: ", data [6][1], '\n'

# 3. How many birds were counted at the last site?
print "# birds at last site: ", data[-1][1], '\n'

# 4. What is the total number of birds counted across all sites?
total_birds = 0
for site in data:
    total_birds += site[1]
print "total number of birds: ", total_birds, '\n'

# 5. What is the average number of birds seen on a site?
print "Average number of birds per site: ", float(total_birds)/(len(data)-1), '\n'
    
# 6. What is the total number of birds counted on sites with codes beginning with C? (don't just identify this sites by eye, in the real world there could be hundreds or thousands of sites)

total_birds_c_site = 0
for site in data:
    if 'C' in site[0]:
        #print site[0], site[1] - just doing paranoid check
        total_birds_c_site += site[1]
print "total number of birds in sites with C: ", total_birds_c_site, '\n'