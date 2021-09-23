import numpy as np

if __name__ == '__main__':
    n,m = list(map(int,input().split()))

    arr = []

    for _ in range(n):
        arr.append(list(map(int,input().split())))

    arr = np.array(arr).reshape(n,m)

    np.set_printoptions(legacy='1.13')

    print(np.mean(arr,axis=1))
    print(np.var(arr,axis=0))
    print(np.std(arr))


