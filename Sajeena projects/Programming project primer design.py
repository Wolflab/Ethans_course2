from __future__ import division 
# Import a fasta file for the purpose of parsing sequence information and generating primers
#count how many records are in the current fasta file 
from Bio import SeqIO
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

#tell me how many records are in my file
filename = "C:\Users\Rene\Dropbox\ls_orchid.fasta" #example fasta file
count = 0
for record in SeqIO.parse(filename, "fasta"):
    count = count + 1
print("1. There were " + str(count) + " records in file " + filename)
print " " 
      
#print all record ids in the fasta file, plus their lengths    
print "2. The fasta file contains the following record ids and lengths of sequences"
handle = open("C:\Users\Rene\Dropbox\ls_orchid.fasta", "rU")
for record in SeqIO.parse(handle,"fasta"):
    print ("%s %i" % (record.id, len(record)))
handle.close()
print " "  

#Create a list, if you want to slice out any pieces or determine largest, smallest, average sequence lengths, etc. . 
from Bio.SeqIO.FastaIO import SimpleFastaParser
with open('C:\Users\Rene\Dropbox\ls_orchid.fasta') as fasta_file: 
    identifiers = []
    lengths = []
    for title, sequence in SimpleFastaParser(fasta_file):
        identifiers.append(title.split(None, 1)[0])
        lengths.append(len(sequence))
print "3. Largest sequence is %s and the smallest sequence is %i" % (max(lengths), min(lengths))
#how to find the associated id?
print " "
 
#printing info on a particular records within this file 
handle = open("C:\Users\Rene\Dropbox\ls_orchid.fasta", "rU")
records = list(SeqIO.parse(handle, "fasta")) #make a fasta file with multiple records into a list for easy access
handle.close()
print "Choose which record to examine in detail, otherwise the following gives the first record's information" 
print " "
print "4. First record information" 
print " " 
print records[0] #examine first record's information, change [] to look at another record
print " " 
print "5. Sequence of first record" # change [] to view the sequence of another record
print " " 
print(records[0].seq) 
print " " 
print "6. Length of first record's sequence is %s" % len(records[0])
print " " 

#generate the first 20 bp as forward primer for a record
print "Generate a forward primer for a given sequence (in this case, 1st record)"
handle = open("C:\Users\Rene\Dropbox\ls_orchid.fasta", "rU")
records = list(SeqIO.parse(handle, "fasta")) #make a fasta file with multiple records into a list for easy access
handle.close()
record = records[0].seq
fwd_primer = record[:20] # you can change 
print " " 
print "7. Forward primer for this record is %s:" % fwd_primer
print " " 
print "   Original sequence of this record is %s" % (records[0].seq)
print " " 

#generate last 20 bp of reverse complement for reverse primer of a particular sequence
rev_complement = record.reverse_complement() #reverse primers are reverse complements of the template strand
rev_primer_location = len(rev_complement)-20 # I chose to make primers of length 20 bp
rev_primer = rev_complement[rev_primer_location:]
print "8. Reverse primer for record is %s:" % rev_primer
print " " 
print "   Original reverse complement of this sequence of this record is %s" % (rev_complement) 

#GC content of forward and reverse   
fwd_C_count = fwd_primer.count('C') 
fwd_G_count = fwd_primer.count('G') 
length = len(fwd_primer) 
fwd_cg_percentage = (float(fwd_C_count + fwd_G_count) / length)*100
rev_C_count = rev_primer.count('C') 
rev_G_count = rev_primer.count('G')
length = len(rev_primer)
rev_cg_percentage = (float(rev_C_count + rev_G_count) / length)*100
print " " 
print "The GC content of the forward primer is %s and the reverse primer is %i" % (fwd_cg_percentage,rev_cg_percentage) 
print " " 
#Calculate the melting temperature of these primers
my_seq_fwd = fwd_primer
my_seq_rev = rev_primer
Tm_fwd = mt.Tm_staluc(my_seq_fwd)
Tm_rev = mt.Tm_staluc(my_seq_rev)
print "The melting temperature of the forward primer is %s and the reverse primer is %i." % (mt.Tm_staluc(my_seq_fwd), mt.Tm_staluc(my_seq_rev)) 
 
#????getting info on records into an excel, see http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/fasta_n/ for example
input_file = open('C:\Users\Rene\Dropbox\ls_orchid.fasta', 'r')  #r means read
output_file = open('programming_fasta_project.tsv','w') #w means let's write the record to a tab delimited file
output_file.write('record_id\tforward\treverse\tTm_f\tTm_r\tLength_fwd\tLength_rev\tCG_fwd\tCG_rev\n') #headers for the output file, In Python (and also the C and C++ programming languages) we must write \t to mean a tab, and \n to mean an end of line (new line) character. i.e. that means:#Gene (tab) A (tab) C (tab) G (tab) T (tab) Length (tab) CG%
for record in SeqIO.parse('C:\Users\Rene\Dropbox\ls_orchid.fasta', "fasta") :
    record_id = records[0].id
    forward = fwd_primer
    reverse = rev_primer
    Tm_f = Tm_fwd
    Tm_r = Tm_rev 
    Length_fwd = len(fwd_primer)
    Length_rev = len(rev_primer) 
    CG_fwd = fwd_cg_percentage
    CG_rev = rev_cg_percentage
    output_line = '%s\t%s\t%s\t%i\t%i\t%i\t%i\t%i\t%i\n' % (record_id, forward, reverse, Tm_f, Tm_r, Length_fwd, Length_rev, CG_fwd, CG_rev)
    output_file.write(output_line) #This line added by Paul
output_file.close()
input_file.close()

















