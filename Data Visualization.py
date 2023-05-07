import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({'x': np.random.normal(0, 1, 100),
                     'y': np.random.normal(0, 1, 100),
                     'z': np.random.normal(0, 1, 100),
                     'category': np.random.choice(['A', 'B', 'C'], 100)})

# Scatter plot using matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(data['x'], data['y'], c=data['z'], cmap='cool')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Colorbar')
plt.show()

# Scatter plot using seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='x', y='y', hue='category', style='category', s=100)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Categories')
plt.show()

# Line plot using matplotlib
plt.figure(figsize=(8, 6))
plt.plot(data['x'], label='X')
plt.plot(data['y'], label='Y')
plt.plot(data['z'], label='Z')
plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Plot')
plt.show()

# Bar chart using matplotlib
plt.figure(figsize=(8, 6))
data['category'].value_counts().plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Bar Chart')
plt.show()

# Histogram using matplotlib
plt.figure(figsize=(8, 6))
plt.hist(data['x'], bins=20)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Box plot using seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='category', y='z')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot')
plt.show()

# Violin plot using seaborn
plt.figure(figsize=(8, 6))
sns.violinplot(data=data, x='category', y='z')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Violin Plot')
plt.show()

# Bubble chart using plotly
fig = px.scatter(data, x='x', y='y', size='z', color='category', hover_data=['x', 'y', 'z'])
fig.update_layout(title='Bubble Chart')
fig.show()
