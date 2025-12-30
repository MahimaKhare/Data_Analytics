import pandas as pd 
df = pd.read_csv("Exam_Score_Prediction.csv")
#print(df.to_string())
print(df.head())
print(df.tail())
#random row 
print(df.sample())
#row and coloumn
print(df.shape)
#column name
print(df.columns)
#index 
print(df.index)
#info(nulls, dtype)
print(df.info())
#
print(df.describe())


