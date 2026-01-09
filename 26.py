#Lineplot in Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset('anagrams')
print(data)

#lineplot
sns.lineplot(x ='subidr',y = 'num1', data = data)
plt.show()

#hue
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr')
plt.show()

#size
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', sizes = (0.8,0.1))
plt.show()

#line style
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr')
plt.show()

#color palette
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent")
plt.show()

#markers
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent", markers= ["o",">"])
plt.show()

#remove dashed line
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent", markers= ["o",">"], dashes= False)
plt.show()

#remove legend
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent", markers= ["o",">"], dashes= False, legend= False)
plt.show()

#grid line
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent", markers= ["o",">"], dashes= False, legend= False)
plt.grid()
plt.show()

#Title
sns.lineplot(x ='subidr',y = 'num1', data = data, hue = 'attnr', style='attnr', palette= "Accent", markers= ["o",">"], dashes= False, legend= False)
plt.grid()
plt.title('Data Chart')
plt.show()

