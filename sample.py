import warnings
import numpy as np
# import matplotlib.pyplot as plt
warnings.filterwarnings("ignore", category=DeprecationWarning)

fs1 = np.fromfile("C:\\years\\year1.txt", dtype=int, sep=",")
fs2 = np.fromfile("C:\\years\\year2.txt", dtype=int, sep=",")
print(type(fs1))
print(fs1)

# print(fs2)
# s1 = np.fromfile("C:\\years\\price.txt", dtype=int,sep=",")
# s2 = np.fromfile("C:\\years\\price2.txt", dtype=int,sep=",")
# print(s1)
# print(s2)

