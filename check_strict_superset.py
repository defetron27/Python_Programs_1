if __name__ == '__main__':
    superSet = set(map(int,input().split()))
    n = int(input())

    strict = []

    for i in range(n):
        subSet = set(map(int,input().split()))

        if len(subSet.difference(superSet)) == 0:
            strict.append(True)
        else:
            strict.append(False)
    if False in strict:
        print(False)
    else:
        print(True)
