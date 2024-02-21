#Import the libraries
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Load Dataset
epl_df = pd.read_csv('EPL 2020_2021.csv')
epl_df.head()

epl_df.info()
epl_df.describe()

#Check for null values
epl_df.isna().sum()

#Create 2 columns
epl_df['MinsPerMatch'] = (epl_df['Mins']/epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals']/epl_df['Matches']).astype(float)
epl_df.head()

#Total Goals
Total_Goals = epl_df['Goals'].sum()
Total_Goals

# %%
