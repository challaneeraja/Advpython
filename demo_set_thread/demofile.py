# import warnings
import numpy as np
import matplotlib.pyplot as plt
# warnings.filterwarnings("ignore", category=DeprecationWarning)

fs1 = np.fromfile(r'C://years//demo1.txt', dtype=int,sep=',')
fs2 = np.fromfile(r'C://years//demo2.txt', dtype=int, sep=",")
sa1 = np.fromfile(r'C://years//sale1.txt',dtype=int,sep=",")
sa2 = np.fromfile(r'C://years//sale2.txt',dtype=int,sep=",")
print(type(fs1))
print(fs1)
print(fs2)
print(sa1)
print(sa2)
plt.plot(fs1,sa1,label="year")
plt.plot(fs2,sa2,label="sales")
plt.xlabel("years of 2001 to 2020")
plt.ylabel("sales from year to year")
plt.legend("right")
plt.show()

# print(fs2)
# s1 = np.fromfile("C:\\years\\price.txt", dtype=int,sep=",")
# s2 = np.fromfile("C:\\years\\price2.txt", dtype=int,sep=",")
# print(s1)
# print(s2)

