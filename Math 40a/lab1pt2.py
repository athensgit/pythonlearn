import worldseries2
import matplotlib.pyplot as plt
import pandas as pd

x = 0

data = []

while x < 44:
    w, l = worldseries2.worldseries(.65, 7)
    better_team_wins = w
    worse_team_wins = l
    x = x + 1
    if w<l:
        print (better_team_wins)
        data.append(better_team_wins)
    if l<w:
        print(worse_team_wins)
        data.append(worse_team_wins)

df = pd.DataFrame(data, columns=['Losses'])

freq = df['Losses'].value_counts().sort_index().reset_index() 
freq.columns = ['Losses', 'Frequency']

print(freq)

plt.bar(freq['Losses'].astype(str), freq['Frequency']) 

"""astype(str) was added because otherwise the x axis is shows up weird with the bars in between full integers"""

plt.xlabel('# of Losses')
plt.ylabel('Frequency')
plt.title('Losing Team Stats')

plt.show()