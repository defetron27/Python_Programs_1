def count_substring(string, sub_string):
    count = 0
    i = 0
    j = 0
    sub = 0
    while i  < len(sub_string):
        while j < len(string):
            if(sub_string[i] == string[j]):
                sub = sub + 1
                j = j+1
                break
            else:
                j = j+1
                sub = 0
                i = 0
        if(sub == len(sub_string)):
            count = count + 1
            sub = 0
            i = 0
            if(len(string)%2 != 0):
                j = j - 1
        else:
            i = i + 1
    return count

