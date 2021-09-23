import numpy as np

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(float,input().split())))

a = np.array(a).reshape(n,n)

res = np.linalg.det(a)

num = str(res-int(res))[1:]

if len(num) > 2:
    print('%.2f'%res)
else:
    print(res)
