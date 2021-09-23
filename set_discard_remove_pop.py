if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for i in range(N):
        lst = list(input().split())
        query = lst[0]
        if len(lst) > 1: value = int(lst[1])
        if query == 'remove':
            if value in s:
                s.remove(value)
        if query == 'discard':
            s.discard(value)
        if query == 'pop':
            if len(s) > 0:
                s.pop()

    if len(s) == 0: 
        print(0)
    else:
        sum = 0
        for i in s:
            sum+=i
        print(sum)

