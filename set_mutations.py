if __name__ == '__main__':
    n = int(input())
    sA = set(map(int,input().split()))

    m = int(input())
    
    for i in range(m):
        lst = input().split()
        sB = set(map(int,input().split()))
        if lst[0] == 'intersection_update':
            sA.intersection_update(sB)
        if lst[0] == 'update':
            sA.update(sB)
        if lst[0] == 'symmetric_difference_update':
            sA.symmetric_difference_update(sB)
        if lst[0] == 'difference_update':
            sA.difference_update(sB)
    
    if len(sA) == 0:
        print(0)
    else:
        sum = 0
        for i in sA:
            sum+=i
        print(sum)

