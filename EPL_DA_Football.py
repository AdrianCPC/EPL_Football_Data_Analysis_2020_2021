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
# %%

epl_df.info()
epl_df.describe()
# %%

#Check for null values
epl_df.isna().sum()
# %%

#Create 2 columns
epl_df['MinsPerMatch'] = (epl_df['Mins']/epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals']/epl_df['Matches']).astype(float)
epl_df.head()

#Total Goals
Total_Goals = epl_df['Goals'].sum()
Total_Goals

# %%

#Penalty Goals
Total_PenaltyGoals = epl_df['Penalty_Goals'].sum()
Total_PenaltyGoals
# %%

#Penalty Attemps
Total_PenaltyAttempts = epl_df['Penalty_Attempted'].sum()
Total_PenaltyAttempts
# %%

#Pie chart for penalties missed vs scored
plt.figure(figsize=(13,6))
pl_not_scored = epl_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data = [pl_not_scored, Total_PenaltyGoals]
labels = ['Penalties missed', 'Penalies Scored']
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors=color, autopct='%.0f%%')
plt.show()
# %%

#Unique positions
epl_df['Position'].unique()
# %%

#Total FW players
epl_df[epl_df['Position'] == 'FW']
# %%

#Players from different nations
np.size((epl_df['Nationality'].unique()))
# %%

#Most players from which countries
nationality = epl_df.groupby('Nationality').size().sort_values(ascending=False)
nationality.head(10).plot(kind='bar', figsize=(12,6), color=sns.color_palette('magma'))
# %%
