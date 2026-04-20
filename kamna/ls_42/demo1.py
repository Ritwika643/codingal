import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import files 
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')
data.head()

mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is -",mean_age)

mean_fare = np.mean(data['Fare'])
print("Mean Fare is -",mean_fare)

meadian_age = np.meadian(data['Age'])
print("Meadian value of Age-",meadian_age)

meadian_fare = np.meadian(data['Fare'])
print("Meadian value of Fare -",meadian_fare)

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender - ",mode_gender)