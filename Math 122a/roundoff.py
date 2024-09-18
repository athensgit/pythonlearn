import random
import math
import matplotlib.pyplot as plt

data = []

def index(newindex, change, baseline):
    return newindex + change * (1000/baseline)

def truncate(num):
    return math.floor(num * 10**3)/10**3

z = 0
newindex = 1000

while z < 2800:

    baseline = 0
    x = 0

    while x < 1400:
        initialprice = 200*random.random()
        baseline += initialprice
        
        x += 1

    change = (4*random.random())-2

    newindex = index(newindex, change, baseline)
    truncate_x = truncate(newindex)
    newindex = truncate_x
    data.append(truncate_x)

    z+=1

print(change)
print(newindex)


plt.xlabel('Number of changes')
plt.ylabel('Index Value')
plt.title('Change in Index Value Over 22 Months')

plt.plot(data)
plt.show()
