#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For data visualization
import seaborn as sns  # For advanced data visualization


# In[2]:


data = pd.read_excel(r'C:\Users\USER\Documents\ORIGINAL DATA DRY SEASON AT PYAKASA STAFF PREMESIS.xlsx')


# In[3]:


data.head()


# In[4]:


# Drop rows with all NaN values
data.dropna(how='all', inplace=True)


# In[5]:


data.head()


# In[6]:


data.columns = data.iloc[0]
data = data[0:]


# In[7]:


data.head(10)


# In[8]:


# Reset the index
data.reset_index(drop=True, inplace=True)


# In[9]:


# Remove the first row after setting the header (which is a duplicate header)
data = data.drop(index=0)  # Drop the first row (index 0)


# In[10]:


data.head(10)


# In[11]:


# Step 1: Calculate Mean
mean_values = data.mean()
print("Mean values:\n", mean_values)

# Step 2: Calculate Median
median_values = data.median()
print("\nMedian values:\n", median_values)

# Step 3: Calculate Standard Deviation
std_dev_values = data.std()
print("\nStandard Deviation values:\n", std_dev_values)


# In[12]:


# Display the column names
print(data.columns)


# In[13]:


# Step 2: Group by the 'TIME' column and compute the mean of 'PM1.0'
grouped_pm = data.groupby('TIME')['PM1.0'].mean().reset_index()

# Display the results
print(grouped_pm)


# In[14]:


# Step 2: Group by the 'TIME' column and compute the mean of 'PM2.5'
grouped_pm = data.groupby('TIME')['PM2.5'].mean().reset_index()

# Display the results
print(grouped_pm)


# In[15]:


# Step 2: Group by the 'TIME' column and compute the mean of 'PM2.5'
grouped_pm = data.groupby('TIME')['PM10'].mean().reset_index()

# Display the results
print(grouped_pm)


# In[16]:


# Step 2: Group by the 'TIME' column and compute the mean of 'PM2.5'
grouped_CO = data.groupby('TIME')['CO'].mean().reset_index()

# Display the results
print(grouped_CO)


# In[17]:


# Line Chart
plt.figure(figsize=(10, 6))
plt.plot(data['TIME'], data['PM1.0'], marker='o')
plt.title('PM1.0 Trends Over Time')
plt.xlabel('Time')
plt.ylabel('PM1.0 Concentration')
plt.grid()
plt.show()


# In[18]:


# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['PM10'], bins=20, color='blue', alpha=0.7)
plt.title('Distribution of PM10 Concentrations')
plt.xlabel('PM10 Concentration')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()


# In[19]:


# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['PM2.5'], data['PM10'], alpha=0.6, color='orange')
plt.title('Scatter Plot of PM2.5 vs PM10')
plt.xlabel('PM2.5 Concentration')
plt.ylabel('PM10 Concentration')
plt.grid()
plt.show()


# In[27]:


data = pd.read_excel(r'C:\Users\USER\Documents\ORIGINAL DATA DRY SEASON AT PYAKASA STAFF PREMESIS.xlsx')


# In[28]:


data.head()


# In[29]:


# Drop rows with all NaN values
data.dropna(how='all', inplace=True)


# In[30]:


data.head()


# In[31]:


data.columns = data.iloc[0]
data = data[0:]


# In[32]:


data.head()


# In[36]:


# Reset the index
data.reset_index(drop=True, inplace=True)


# In[37]:


# Remove the first row after setting the header (which is a duplicate header)
data = data.drop(index=0)  # Drop the first row (index 0)


# In[38]:


data.head()


# In[39]:


# Ensure TIME is treated as integer
data['TIME'] = data['TIME'].astype(int)

# Check if 'PM2.5' exists
if 'PM2.5' in data.columns:
    # Bar Chart for PM2.5
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['TIME'], y=data['PM2.5'], palette='viridis')
    plt.title('PM2.5 Concentration Over Time')
    plt.xlabel('Time (Integer Values)')
    plt.ylabel('PM2.5 Concentration')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# In[ ]:




