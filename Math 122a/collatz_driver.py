import matplotlib.pyplot as plt
from collatz_skeleton import *

collatz_list, collatz_len = collatz(10)
plt.plot(collatz_list)
plt.show()
