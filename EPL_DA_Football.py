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

#Clubs with maximum players in their squad
epl_df['Club'].value_counts().nlargest(5).plot(kind='bar', color=sns.color_palette('viridis'))
# %%

#Clubs with leastt players in their squad
epl_df['Club'].value_counts().nsmallest(5).plot(kind='bar', color=sns.color_palette('viridis'))

# %%

#Players based on age group
Under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] > 20) & (epl_df['Age'] <= 25)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
Above30 = epl_df[epl_df['Age'] > 30]

x = np.array([Under20['Name'].count(), age20_25['Name'].count(),age25_30['Name'].count(),Above30['Name'].count()])
mylabels = ['<=20','>20 & <=25','>25 & <=30', '>30']
plt.title('Total players with Age Groups', fontsize=20)
plt.pie(x, labels = mylabels, autopct='%.1f%%')
plt.show()
# %%

#Total under 20 players in each club
players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind='bar', color= sns.color_palette('cubehelix'))

# %%

#Under 20 players in ManU
players_under_20[players_under_20['Club'] == 'Manchester United']

# %%

#Under 20 players in Chelsea
players_under_20[players_under_20['Club'] == 'Chelsea']

# %%

#Average age of players in each club
plt.figure(figsize=(12,6))
sns.boxplot(x='Club', y='Age', data=epl_df)
plt.xticks(rotation=90)
plt.show()


# %%
#Average age from all clubs
num_player = epl_df.groupby('Club').size()
data = (epl_df.groupby('Club')['Age'].sum())/num_player
data.sort_values(ascending=False)
# %%

#Total assists from  each club
Assits_by_clubs = pd.DataFrame(epl_df.groupby('Club', as_index=False)['Assists'].sum())
sns.set_theme(style='whitegrid',color_codes=True)
ax=sns.barplot(x='Club', y='Assists',data=Assits_by_clubs.sort_values(by='Assists'),palette='Set2')
ax.set_xlabel('Club',fontsize=30)
ax.set_ylabel('Assists', fontsize=20)
plt.xticks(rotation=75)
plt.rcParams['figure.figsize'] = (20,8)
plt.title('Plot of Club vs Total Assits', fontsize=20)
plt.show()
# %%

#Top 10 Assists
top_10_assists = epl_df[['Name','Club','Assists','Matches']].nlargest(n=10,columns='Assists')
top_10_assists
# %%

#Total Goals each Club
Goals_by_clubs = pd.DataFrame(epl_df.groupby('Club', as_index=False)['Goals'].sum())
sns.set_theme(style='whitegrid',color_codes=True)
ax=sns.barplot(x='Club',y='Goals',data=Goals_by_clubs.sort_values(by='Goals'),palette='rocket')
ax.set_xlabel('Club',fontsize=30)
ax.set_ylabel('Goals',fontsize=20)
plt.xticks(rotation=75)
plt.rcParams['figure.figsize'] = (20,8)
plt.title('Plot of Clubs vs Total Goals', fontsize=20)
# %%

#Most goals by players
top_10_goals = epl_df[['Name','Club','Goals','Matches']].nlargest(n=10,columns='Goals')
top_10_goals
# %%
