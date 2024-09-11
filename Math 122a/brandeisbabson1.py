import numpy as np
data = np.loadtxt('brandeisbabson.txt',encoding='utf-16')

import pandas as pd
df = pd.DataFrame(data)

import matplotlib.pyplot as plt

df.columns = ['No.', 'Year', 'Brandeis Score', 'Babson Score']
difference = df['Brandeis Score'] - df['Babson Score']

def winnercalc(difference):
    if difference > 0:
        return 1
    elif difference < 0:
        return -1
    else:
        return 0

winner_tally = difference.apply(winnercalc)

new_columns = {'Difference': difference, 'Winner Tally': winner_tally}

df = df.assign(**new_columns)

df.to_csv('brandeisbabsonwinners.txt', index=False, sep=' ', header=True)

year = df['Year']

print(df)

plt.scatter(year, winner_tally)

x =[]
y=[]

for year in range(1992, 2022):
    df_year = df[df['Year'] == year]
    print(df_year)
    
    x += list(df_year['Year'])
    y += list(df_year['Winner Tally'])
    
plt.scatter(x, y, c = 'red')
plt.show()