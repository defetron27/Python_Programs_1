import numpy as np

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    arr = np.array(arr)
    arr.shape = (3,3)
    print(arr)
