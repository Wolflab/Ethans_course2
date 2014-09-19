import pandas as pd

data = pd.read_csv('TradeoffData.csv')

print "number unique treatments: ", len(data.groupby(['Treatment']))

print "number unique Groups: ", len(data.groupby(['Group']))