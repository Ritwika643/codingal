from kagglehub.packages import KAGGLEHUB_REQUIREMENTS_FILENAME
#Activity- 1 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import kagglehub 
from kagglehub import KaggleDatasetAdapter

dataset = "vedavyasv/usa-housing"
file_path= "USA_Housing.csv"
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    dataset,
    file_path
)
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)
sns.pairplot(df.select_dtypes(include=[np.number]))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(),annot=True)
plt.show()