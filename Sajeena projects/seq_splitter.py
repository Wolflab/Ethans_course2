

data = open('fasta', 'rU')
newfile = open('short_seq.txt', 'w')

max_seq_length = 1000

for line in data:
    if line[0] == '>':
        header = line.strip()
    else:
        #seq = line
        count = 1
        for i in xrange(0,len(line),max_seq_length):
            new_header = header + "_" + str(count) + '\n'
            new_seq = line[i:i+max_seq_length] + '\n'
            newfile.write(new_header)
            newfile.write(new_seq)
            count+=1
data.close()
newfile.close()
        