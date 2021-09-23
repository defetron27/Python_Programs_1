def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):
        if string[i] in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart+= len(string) - i
    
    if stuart == kevin:
        print("Draw")
    elif stuart>kevin:
        print("Stuart " + str(stuart))
    else:
        print("Kevin " + str(kevin))

