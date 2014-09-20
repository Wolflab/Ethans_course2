import pandas as pd

data = pd.read_csv('TradeoffData.csv')


for row in data['RelativeFitness']:
    if row > 1.0:
        print row

#
#
#
#print "number unique treatments: ", len(data.groupby(['Treatment', 'Group']))

#print "number unique Groups: ", len(data.groupby(['Group']))

#b = data[data['Group'] == 'BKB']
#print len(b)

#print b[['RelativeFitness','Replicate']] #.iloc[0:1]

