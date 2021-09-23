def print_rangoli(size):
    total = (size + size - 1)
    total = total + (total - 1)
    for i in range(size,0,-1):
        str = ""
        for j in range(size,i-1,-1):
            str = str + chr(96+j) + "-"
        for k in range(i+1,size+1):
            str = str + chr(96+k) + "-"
        print(str.center(total,"-")[:total])
    for i in range(1,size):
        str = ""
        for j in range(size,i+1,-1):
            str = str + chr(96+j) + "-"
        for k in range(i+1,size+1):
            str = str + chr(96+k) + "-"
        print(str.center(total,"-")[:total])

