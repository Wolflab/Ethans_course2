import string
#testing removal of eod of line chars

seq = 'gggggaaaaa\ntttttccccc'

seq2 = seq.replace('\n', '').replace('\r', '')


print seq2