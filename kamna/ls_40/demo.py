import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import kagglehub
from kagglehub import KaggleDatasetAdapter

dataset = "aariyan101/usa-housingcsv"
file_path= "USA_Housing.csv"
HouseDF = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    dataset,
    file_path
)

print(HouseDF.head())

HouseDF.head()

HouseDF.info()

HouseDF.columns

sns.pairplot(HouseDF)

numeric_df = HouseDF.select_dtypes(include=[np.number])
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(),annot=True,cmap='coolwarm')
numeric_df= HouseDF.select_dtypes(include=[np.number])
plt.figure(figsize=(8,6))
sns.scatterplot(x='Avg. Area Income', y='Price', data= HouseDF)
plt.title('Income vs Price')
plt.show()