import worldseries1 
import matplotlib.pyplot as plt

data = []

x = 0

while x < 4399:
    w, l = worldseries1.worldseries(.65, 7)
    better_team_wins = w
    worse_team_wins = l
    x = x + 1
    if w<l:
        print (better_team_wins)
        data.append(better_team_wins)
    if l<w:
        print(worse_team_wins)
        data.append(worse_team_wins)

plt.hist(data, bins=4, color='skyblue', edgecolor='black')

plt.xlabel('Number of losses')
plt.ylabel('Frequency')
plt.title('Losing Team Statistics')

plt.show()


   



