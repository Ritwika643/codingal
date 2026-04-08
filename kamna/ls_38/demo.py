import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()

file_name=list(uploaded.keys())[0]

countries = pd.read_csv(file_name)

print(countries.head())

c_52 = countries.loc[countries['year'] == 1952]
c_07 = countries.loc[countries['year'] == 2007]

c_merge = c_52.merge(c_07, on ='country')

c_merge = c_merge.drop(['year_x', 'year_y'],axis=1)

c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']

c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)

names = c_merge['country']
pop_grow = c_merge['population_growth'] / 10**6

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)

plt.xlabel('Country')
plt.ylabel('Population Growth in (Millions)')
plt.title('Top 10 Countries with Biggest Population Growth (1952-2007)')
plt.xticks(rotation=45)

for x,y in zip(names, pop_grow):
  label = "(1.2f)".format(y)
  plt.annotate(label,
               (x,y),
               textcoords="offset points",
               xytext=(0,10),
               ha='center')
  plt.show()