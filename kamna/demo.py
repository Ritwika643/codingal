import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

dataset_name = "ashokkumarbibbab/country-vaccination"

path = kagglehub.dataset_download(dataset_name)

files = os.listdir(path)
print("Files in the dataset:", files)

csv_files = [f for f in files if f.endswith('.csv')]
if not csv_files:
    raise FileNotFoundError(f"No CSV files found in the dataset '{dataset_name}' at {path}")

file_path = csv_files[0] 
print(f"Using file: {file_path}")

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    dataset_name,
    file_path
)

print("First 5 records:")
print(df.head())
df.head(10)
df.isnull().any()
subset=df.iloc[:5200,:]
plt.figure(figsize=(12,8))
sns.heatmap(subset.isnull(),cbar=False , cmap='viridis')
plt.show()
df.head(10)
df=df.dropna(how='all')
df=df.fillna(method="bfill")
df=df.interpolate(numeric_only=True)
df_dropped=df.dropna
df_dropped