import numpy as np

if __name__ == '__main__':
    n = int(input())

    a = []
    b = []

    for _ in range(n):
        a.append(list(map(int,input().split())))
    
    for _ in range(n):
        b.append(list(map(int,input().split())))

    a = np.array(a).reshape(n,n)
    b = np.array(b).reshape(n,n)

    print(np.dot(a,b))

