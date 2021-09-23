import numpy as np

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = np.array(a)
b = np.array(b)

c = np.transpose(a)
d = np.transpose(b)

print(np.inner(c,b))
print(np.outer(a,d))

