import numpy as np

if __name__ == '__main__':
    n,m,p = map(int,input().split())

    nList = []
    mList = []

    for i in range(n):
        nList.append(list(map(int,input().split())))
    
    for j in range(m):
        mList.append(list(map(int,input().split())))
    
    nArr = np.array(nList)
    mArr = np.array(mList)

    print(np.concatenate((nArr,mArr),axis=0))




