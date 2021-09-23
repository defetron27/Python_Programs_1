import numpy as np

if __name__ == '__main__':
    n,m = list(map(int,input().split()))

    arr = []

    for _ in range(n):
        arr.append(list(map(int,input().split())))

    arr = np.array(arr).reshape(n,m)

    mini = np.min(arr,axis=1)

    print(np.max(mini))



