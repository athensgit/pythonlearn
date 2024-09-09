import worldseries1 
import matplotlib.pyplot as plt

data = []

x = 0

while x < 4399:
    w, l = worldseries1.worldseries(.65, 7)
    losing_team_wins1 = w
    losing_team_wins2 = l
    x = x + 1
    if w<l:
        print (losing_team_wins1)
        data.append(losing_team_wins1)
    if l<w:
        print(losing_team_wins2)
        data.append(losing_team_wins2)

plt.hist(data, bins=4, color='skyblue', edgecolor='black')

plt.xlabel('Number of losses')
plt.ylabel('Frequency')
plt.title('Losing Team Statistics')

plt.show()


   



