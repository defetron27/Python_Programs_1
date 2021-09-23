def pattern(n,m):
    mid = (n+1) // 2
    j = 1
    c = '.|.'

    for i in range(1,n+1):
        if i == mid:
            print("WELCOME".center(m,'-'))
            j = j-2
        elif i > mid:
            print((c*j).center(m,'-'))
            j = j-2
        else:
            print((c*j).center(m,'-'))
            j = j+2

if __name__ == '__main__':
    n,m = input().split()
    pattern(int(n),int(m))


    
