import numpy as np
import matplotlib.pyplot as plt
num=np.fromfile("C:/data/test.txt",dtype=int,sep=",")
items=np.genfromtxt("C:/New folder1/first.txt",dtype='str',delimiter=",")
print(items)
print(num)
x=np.arange(len(items))
plt.bar(x,items)
plt.xticks(x,items)
plt.ylabel("numbers")
plt.xlabel("items")
plt.show()