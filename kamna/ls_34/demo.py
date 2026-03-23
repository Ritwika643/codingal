import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

sns.set(style="ticks")

path = kagglehub.dataset_download("muthuj7/weather-dataset")

files = os.listdir(path)
print("Files:", files)

file_path = [f for f in files if f.endswith(".csv")][0]

weather = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "muthuj7/weather-dataset",
  file_path
)

print(weather.head())
print(weather.info())
print(weather.columns)

sns.barplot(x=weather['Humidity'],y= weather['Temperature(C)'])
plt.show()

sns.histplot(weather['Humidity'], kde = True)
plt.show()

sns.histplot(weather['Humidity'], kde = False)
plt.show()

sns.jointplot(x=weather['Humidity'],y= weather['Temperature(C)'])
plt.show()

sns.jointplot(x=weather['Humidity'],y= weather['Temperature(C)'] , kind='hex')
plt.show()

sns.jointplot(x=weather['Humidity'],y= weather['Temperature(C)'] , kind = 'kde')
plt.show()

sns.pairplot(weather['Humidity','Temperature(C)','Pressure(millibars)'])
plt.show()

sns.stripplot(x=weather['summary'],y= weather['Temperature(C)'],jitter = True)
plt.xticks(rotations=45)
plt.show()

sns.swarmplot(x=weather['Humidity'],y= weather['Temperature(C)'])
plt.show()
