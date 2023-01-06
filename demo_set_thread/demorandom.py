import numpy as np
num1=np.random.rand(3)  #generate the one dim random number
num2=np.random.rand(3,2) #shape of array
print(num2)
print(num1)
num3=np.random.randn(5,2)
print(num3)
num4=np.random.randint(3,size=(2,4))
print(num4)
print(np.random.random(3)) # 0.0 to 1.0 it will print
print(np.random.sample(size=(3,2,3)))