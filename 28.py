import matplotlib.pyplot as plt
import seaborn as sns
#countplot
data = sns.load_dataset('anagrams')
print(data)

sns.countplot(x = 'num1', data= data,)
plt.show()

#hue
sns.countplot(x = 'num1', data= data, hue = 'attnr')
plt.show()

#palette
sns.countplot(x = 'num1', data = data, hue = 'attnr', palette = 'dark')
plt.show()

#vars
sns.countplot(x = 'num1', data = data, hue = 'attnr', palette = 'dark',)
plt.show()

#catplot
sns.catplot(x = 'num1', data = data, kind = 'count')
plt.show()
