# DATA LOADING

# pd.read_csv()   -> CSV file load karta hai
# df = pd.read_csv("Heart_Disease_Prediction.csv")

#####################################################################################

# DATA VIEW & STRUCTURE

# df.head()       -> First 5 rows
# df.tail()       -> Last 5 rows
# df.sample()    -> Random rows
# df.shape       -> Rows & columns
# df.columns     -> Column names
# df.index       -> Index info
# df.info()      -> Summary (nulls, dtype)
# df.describe()  -> Numeric stats


########################################################################

# DATA TYPES & SELECTION

# df.dtypes                 -> Column data types
# df.select_dtypes()        -> Type based selection
# df["col"]                 -> Single column
# df[["c1","c2"]]            -> Multiple columns
# df.loc[]                  -> Label based selection
# df.iloc[]                 -> Index based selection
# df.at[]                   -> Fast single value access
# df.iat[]                  -> Fast index based access


# ex. 

# df.select_dtypes(include="number")
# df.loc[0, "age"]
# df.iloc[0, 1]




##################################################################################

# df.isnull()               -> Missing values
# df.notnull()              -> Non-missing
# df.isnull().sum()         -> Missing count
# df.dropna()               -> Drop missing rows
# df.fillna()               -> Fill missing values

# ex.

# df.isnull().sum()
# df["cholesterol"].fillna(df["cholesterol"].median(), inplace=True)



########################################################################################

# DUPLICATE DATA

# df.duplicated()           -> Duplicate rows
# df.duplicated().sum()     -> Count duplicates
# df.drop_duplicates()      -> Remove duplicates

# ex.

# df.drop_duplicates(inplace=True)


############################################################################################################
# DATA CLEANING & TRANSFORMATION

# df.rename()               -> Rename columns
# df.drop()                 -> Drop rows/columns
# df.replace()              -> Replace values
# df.astype()               -> Change dtype
# df.copy()                 -> Copy dataframe


# df.rename(columns={"HeartDisease":"target"}, inplace=True)
# df.replace({"Yes":1,"No":0}, inplace=True)
# df["age"] = df["age"].astype(int)


#######################################################################################


# BASIC ANALYSIS

# df.value_counts()         -> Category count
# df.nunique()              -> Unique count
# df.unique()               -> Unique values
# df.sort_values()          -> Sorting
# df.max() / min()          -> Max / Min
# df.mean()                 -> Mean
# df.median()               -> Median
# df.mode()                 -> Mode
# df.quantile()             -> Percentiles


# ex. 

# df["target"].value_counts()
# df.sort_values("age", ascending=False)



# ################################################################

# CONDITIONAL FILTERING

# df[condition]             -> Filter rows
# & (AND)                   -> Multiple conditions
# | (OR)                    -> OR condition

# df[df["age"] > 50]
# df[(df["age"] > 50) & (df["target"] == 1)]


# ##################################################################################

# DATE & TIME HANDLING

# pd.to_datetime()          -> Convert to date
# .dt.year                  -> Extract year
# .dt.month                 -> Extract month
# .dt.day                   -> Extract day

# df["date"] = pd.to_datetime(df["date"])
# df["year"] = df["date"].dt.year



# ########################################################

# DATA EXPORT

# df.to_csv()               -> Save CSV

# df.to_csv("clean_data.csv", index=False)
