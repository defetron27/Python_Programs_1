import numpy as np

if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    arr = np.array(arr)
    print(np.transpose(arr))
    print(arr.flatten())
