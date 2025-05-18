### Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 
import os
 
 # Create a directory to save plots output_dir = "outputs"
 os.makedirs(output_dir, exist_ok=True)

# Load Iris dataset
try:
 iris = load_iris()
 df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
 df['species'] = iris.target
 df['species'] = df['species']. map(dict(zip(range(3), iris.target_names)))
except Exception as e:
 print(f"Error loading dataset: {e}")
 exit()

 #Task !: Explore Dataset
 print("First 5 rows of dataset:")
 print(df.head())

 print("\nDataset Info:")
 print(df.isnull().sum())

 # Clean Data: (Iris dataset is clean but check just in case)
 df.dropna(inplace=True)

 # Task 2: Basic Statistics 
 print("\nBasic Statistics")
 print(df.describe())

 # Group by species and compute mean
 grouped = df.groupby('species').mean()
 print("\nMean values by species:")
 print(grouped)

 # Task 3: Visualisation

 # 1. Line Plot - Mean values per species 
 grouped.plot(kind='line', marker='o', title='Mean Feature Values per Species')
 plt.ylabel("Feature")
 plt.grid(True)
 plt.savefig(os.path.join(output_dir, "line_plot.png"))
 plt.show()

 # 2. Bar Chart - Average petal lenght per species 
 sns.barplot(x='species', y='petal lenght (cm)', data=df)
 plt.title("Average Petal Lenght per species")
 plt.savefig(os.path.join(output_dir, "bar_chart.png"))
 plt.show()

 # 3. Histogram - Sepal Lenght Distribution
 plt.hist(df['sepal lenght (cm)'] bins=15, color='skyblue', edgecolor='black')
 plt.title("Distribution of sepallenght")
 plt.xlabel("Sepal Lenght (cm)")
 plt.ylabel("Frequency")
 plt.savefig(os.path.join(output_dir, "scatter_plot.png"))
 plt.show()

 # 4. Scatter Plot - Sepal Lenght vs Petal Lenght
 sns.scatterplot(x='sepal lenght (cm)', y=petal lenght (cm)), hue=species', data=df)
 plt.title("Sepal Lenght vs Petal Lenght")
 plt.savefig(os.path.join(output_dir, "scatter_plot.png"))
 plt.show()

 # Save cleaned data
 df.to_csv(os.path.join(output_dir, "cleaned_iris.csv"), index=False)

 print("\nAll plots and cleaned data have been saved in the 'outputs' directory.")