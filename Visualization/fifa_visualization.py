from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df['Total'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.8)

f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data=df, x='Year', y='Total')
plt.show()
ax.set_title('Goals scored in World Cup Matches by year')

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
sns.set_context('notebook',font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goals per year')
plt.show()