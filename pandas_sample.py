import pandas as pd

data = pd.read_csv('data/data.csv', header=0, names=['Id', 'Name', 'Age', 'Job'], na_values=['?', 'NA'])
print(data.head())
print(data.info())
print(data.describe())