
f = open('rps.txt')
p = 0
while 1:
    char = f.read(1)
    if(char==''):
        break
    f.read(1)
    c2=f.read(1)
    f.read(1)
    #rock
    if(char=='A'):
        #lose
        if(c2=='X'):
            p += 3 + 0
        #draw
        if(c2=='Y'):
            p += 1 + 3
        #win
        if(c2=='Z'):
            p += 2 + 6
    #paper
    if(char=='B'):
        #lose
        if (c2 == 'X'):
            p += 1 + 0
        #draw
        if (c2 == 'Y'):
            p += 2 + 3
        #win
        if (c2 == 'Z'):
            p += 3 + 6
    #scissors
    if (char == 'C'):
        #lose
        if (c2 == 'X'):
            p += 2 + 0
        #draw
        if (c2 == 'Y'):
            p += 3 + 3
        #win
        if (c2 == 'Z'):
            p += 1 + 6
print(p)
