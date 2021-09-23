

# Complete the solve function below.
def solve(s):
    list = s.split()
    string = s
    for i in list:
        if(not i.isdigit()):
            j = i[0].upper()
            string = string.replace(i,j + i[1:])
    return string
    

