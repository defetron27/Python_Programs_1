def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year >= 1900 and (year/4).is_integer() == True):
        if((year/100).is_integer() == True):
            if((year/400).is_integer() == True):
                leap = True
        elif((year/400).is_integer() == False):
                leap = True

    
    return leap

