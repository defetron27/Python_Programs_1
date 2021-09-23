if __name__ == '__main__':
    n = int(input())
    count = set()
    for i in range(n):
        count.add(input())
    
    print(len(count))
