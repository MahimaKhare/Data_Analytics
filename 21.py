import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')
#print(df)

#empty cells
#remove row
df.dropna()

#replace empty value
df.fillna(130, inplace = True)


#wrong data
avg = 0 
for x in df.index:
    #print(df.loc[x,'Calories'])
    if df.loc[x, 'Calories'] < 400:
        avg = df.loc[x, 'Calories']
       # print(np.mean(avg))
    if df.loc[x,'Calories'] > 400:
        df.loc[x, 'Calories'] = avg


# 
avg = 0         
for x in df.Calories:
    #print(x)
    if x < 400:
        avg = x
        print(np.mean(avg))

   