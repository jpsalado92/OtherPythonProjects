# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
print(X = dataset.iloc[:, :-1].values)
print(y = dataset.iloc[:, -1].values)



