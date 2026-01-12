import seaborn as sns
import matplotlib.pyplot as plt

#data = sns.load_dataset('anscombe')
#print(data)

#histogram
"""sns.displot(data['x'])
plt.show()

#bins
sns.displot(data['x'],bins = 4)
plt.show()

sns.displot(data['x'], bins = [10,12,16,22])
plt.show()

#Curve
sns.displot(data['x'], bins = [10,12,16,22], kde = True )
plt.show()

#rug
sns.displot(data['x'], bins = [10,12,16,22], kde = True, rug = True )
plt.show()

#color
sns.displot(data['x'], bins = [10,12,16,22], kde = True, rug = True, color = 'r')
plt.show()

#log_scale
sns.displot(data['x'],kde = True, rug= True, log_scale= True)
plt.show()"""

#barplot
"""data = sns.load_dataset('attention')
print(data.head(5))

sns.barplot(x='subject',y='score',data = data)
plt.show()

#hue
sns.barplot(x='subject',y='score',data = data, hue = 'attention')
plt.show()

#order
sns.barplot(x='subject',y='score',data = data, hue = 'attention', order = ('focused', 'divided'))
plt.show()

#orient
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h')
plt.show()

#color
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h', color= 'g')
plt.show()

#saturation
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h', color= 'g', saturation= 0.5)
plt.show()

#errcolor
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h', color= 'g', saturation= 0.5, errcolor= 'r')
plt.show()

#capsize
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h', color= 'g', saturation= 0.5, errcolor= 'r', capsize= 5)
plt.show()

#dodge
sns.barplot(x='subject',y='score',data = data, hue = 'attention', orient= 'h', color= 'g', saturation= 0.5, errcolor= 'r', capsize= 5, dodge= False)
plt.show()"""

#Scatter plot
data = sns.load_dataset('car_crashes')
print(data.head(5))

sns.scatterplot(x = 'speeding', y = 'alcohol', data= data)
plt.show()

#hue
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev')
plt.show()

#style
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev', style= 'abbrev')
plt.show()

#size
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev', style= 'abbrev', size = 'abbrev' )
plt.show()

#palette
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev', style= 'abbrev', size = 'abbrev', palette = 'dark')
plt.show()

#alpha
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev', style= 'abbrev', size = 'abbrev', palette = 'dark', alpha = 0.4)
plt.show()

#markers
sns.scatterplot(x = 'speeding', y = 'alcohol', data= data, hue ='abbrev', style= 'abbrev', size = 'abbrev', palette = 'dark', alpha = 0.4, markers= ['*','.','o'])
plt.show()

