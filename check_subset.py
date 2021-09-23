if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        aN = int(input())
        a = set(map(int,input().split()))
        bN = int(input())
        b = set(map(int,input().split()))
        if len(a.difference(b)) == 0:
            print(True)
        else:
            print(False)
