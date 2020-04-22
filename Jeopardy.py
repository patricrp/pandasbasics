import pandas as pd

df = pd.read_csv('jeopardy.csv')
print(df.head())

df = df.rename(columns={' Air Date': 'Air Date', ' Round ': 'Round', ' Category': 'Category', ' Value': 'Value', ' Question': 'Question', ' Answer': 'Answer'})
print(df.columns)

words = ["King", "England"]

#Filter DataFrame by words in df['Question']

def filtContent(df, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  
  return df.loc[df['Question'].apply(filter)]

filtered = filtContent(df, words)
print(filtered)

#Casting df['Value']

df['Value'] = df['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)

print(df.Value.head())

#Filtered df by 'King'
words = ['King']
filtered = filtContent(df, words)

#Mean score of questions including 'King'
m = filtered['Value'].mean()
print(m)

#Counting values for all questions
def counting(df):
  return df['Answer'].value_counts()

count = counting(df)
print(count)