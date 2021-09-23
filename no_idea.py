if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    aSet = set(map(int,input().split()))
    bSet = set(map(int,input().split()))

    happiness = 0

    for i in arr:
        if i in aSet:
            happiness += 1
        elif i in bSet:
            happiness -= 1

    print(happiness)
