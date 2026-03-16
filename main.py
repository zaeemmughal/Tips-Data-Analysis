import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print("First 5 rows:")
print(tips.head())

print("\nDataset shape:")
print(tips.shape)

print("\nBasic statistics:")
print(tips.describe())

print("\nMissing values:")
print(tips.isnull().sum())

tips['tip_percent'] = (tips['tip'] / tips['total_bill']) * 100

print("\nNew column added: tip_percent")
print(tips[['total_bill', 'tip', 'tip_percent']].head())

print("\nAverage Tip:", tips['tip'].mean())
print("Average Bill:", tips['total_bill'].mean())

print("\nAverage Tip by Gender:")
print(tips.groupby('sex')['tip'].mean())

print("\nAverage Tip by Day:")
print(tips.groupby('day')['tip'].mean())

print("\nAverage Tip by Smoker:")
print(tips.groupby('smoker')['tip'].mean())

plt.figure()
plt.hist(tips['total_bill'], bins=20)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(tips['total_bill'], tips['tip'])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

day_avg = tips.groupby('day')['tip'].mean()

plt.figure()
plt.bar(day_avg.index, day_avg.values)
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()

correlation = tips[['total_bill', 'tip', 'size']].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure()
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.show()
  
print("\nEDA Completed Successfully!")
