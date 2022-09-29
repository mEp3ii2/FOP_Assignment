import numpy as np

a = np.zeros((1000,1000))
print(a.shape)

a[0][50]=5
a[1][500]=10
a[999][0]=1
a[0][0]=2
print(a[0][50])

print(a[1][500])
print(a[999][0])
print(a)



