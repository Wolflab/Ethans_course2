import pandas as pd


data = pd.read_csv('TradeoffData.csv')
#print data
data2 = data[['Group','RelativeFitness']]
#print data2
for row in data2['RelativeFitness']:
    print row  
    for row in data2.values:
        print row  
\
#
#
#print "number unique treatments: ", len(data.groupby(['Treatment', 'Group']))

#print "number unique Groups: ", len(data.groupby(['Group']))

#b = data[data['Group'] == 'BKB']
#print len(b)

#print b[['RelativeFitness','Replicate']] #.iloc[0:1]

