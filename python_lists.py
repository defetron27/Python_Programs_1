if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(0,N):
        query = raw_input().split()
        name,values = query[0],query[1:]
        values = map(int,values)
        if name == "insert":
            list.insert(values[0],values[1])
        elif name == "print":
            print(list)
        elif name == "remove":
            list.remove(values[0])
        elif name == "append":
            list.append(values[0])
        elif name == "sort":
            list.sort()
        elif name == "pop":
            list.pop()
        else:
            list.reverse()
