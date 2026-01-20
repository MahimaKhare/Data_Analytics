import pandas as pd 
import numpy as np

#series
a = np.array([1,7,8])
print(pd.Series(a))

#Labels:
a = np.array([1,7,2])
a1 = pd.Series(a)
print(a1[0])

#create lables:
a = np.array([1,7,2])
data = pd.Series(a,index = ("x","y","z"))
print(data["y"])

x = {"a":1,
     "b":2,
     "c":4}
data = pd.Series(x)
print(data)

#2d_array
df = pd.read_csv("Exam_Score_Prediction.csv")
print(df.to_string())

#dataframe
print(pd.DataFrame(data))

#Locate row
print(df.loc(0))

#head
print(df.head())

#tail
print(df.tail())

