def swap_case(s):
    string = ""
    for i in s:
        if i.islower() == True:
            string+=i.upper()
        elif i.isupper() == True:
            string+=i.lower()
        else:
            string+=i
    return string

