if __name__ == '__main__':
    stud = []
    arr = []
    low = 0.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud.append([name,score])
    for i in range(len(stud)):
        for j in range(i+1,len(stud)):
            if stud[i][1] > stud[j][1]:
                temp = stud[i]
                stud[i] = stud[j]
                stud[j] = temp

    for i in range(len(stud)):
        if stud[i][1] not in arr:
            arr.append(stud[i][1])

    low = arr[1]

    stud.sort()

    for i in range(len(stud)):
        if stud[i][1] == low:
            print(stud[i][0])

    

