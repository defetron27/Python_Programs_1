import numpy as np

if __name__ == '__main__':
    n,m = map(int,input().split())

    aLst= []
    bLst = []

    for i in range(n):
        aLst.append(list(map(int,input().split())))
    
    for j in range(n):
        bLst.append(list(map(int,input().split())))

    a = np.array(aLst).reshape(n,m)
    b = np.array(bLst).reshape(n,m)

    print(np.add(a,b))
    print(np.subtract(a,b))
    print(np.multiply(a,b))
    print(a//b)
    print(np.mod(a,b))
    print(np.power(a,b))


