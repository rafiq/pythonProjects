import numpy as np
import matplotlib.pyplot as plt
data  = np.loadtxt("Math221_swissbanknotes.txt")

# print(data)

plt.figure()
plt.hist(data[:,3],bins=4)
plt.title('a histogram')
plt.xlabel('values')
plt.ylabel('Freq')
plt.show()

plt.figure()
plt.scatter(data[:,0],data[:,1])
plt.show()