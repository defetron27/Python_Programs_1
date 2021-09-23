import numpy as np

if __name__ == '__main__':
    n,m = map(int,input().split())
    np.set_printoptions(legacy='1.13')
    print(np.eye(n,m))
    


