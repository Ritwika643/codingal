import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import files 
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

data.dtypes

data.isnull().sum()
data.info()