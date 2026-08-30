import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/alish/Downloads/Numpy/Project/employee_data.csv")
print(df.head())

#Checking missing values:
print(df.isnull().sum())

#Replacing Infinite values:
df.replace([np.inf, -np.inf], np.nan, inplace=True)

#Filling missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Experience (Years)'] = df['Experience (Years)'].fillna(df['Experience (Years)'].median())

#remove duplicate records:
df.drop_duplicates(inplace=True)
print(df.isnull().sum())

#Fixing negative salaray:
df['Salary'] = np.where(df['Salary']<0, df['Salary'].mean(), df['Salary'])

#Removing where salary is too much or too low
salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df['Salary'] >= lower_bound) & (df['Salary']<= upper_bound)]

df.to_csv('employee_data.csv', index=False)
print("Data has been cleaned")