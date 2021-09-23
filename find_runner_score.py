if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    a = []

    
    for i in arr:
        if i not in a:
            a.append(i)

    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    
    print(a[len(a) - 2])
            


