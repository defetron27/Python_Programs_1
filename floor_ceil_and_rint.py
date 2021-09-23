import numpy as np

if __name__ == '__main__':
    arr = list(map(float,input().split()))

    a = np.array(arr)

    np.set_printoptions(legacy='1.13')

    print(np.floor(a))
    print(np.ceil(a))
    print(np.rint(a))



