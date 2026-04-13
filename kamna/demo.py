import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from google.colab import files

uploaded = files.upload()

file_name = list(uploaded.keys())[0]

HouseDF = pd.read_csv(file_name)

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
sns.scatterplot(x='Avg.Area Income', y='Price', data= HouseDF)
plt.title('Income vs Price')
plt.show()