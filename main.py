
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
        #rock
        if(c2=='X'):
            p += 1 + 3
        #paper
        if(c2=='Y'):
            p += 2 + 6
        #scissors
        if(c2=='Z'):
            p += 3 + 0
    #paper
    if(char=='B'):
        #rock
        if (c2 == 'X'):
            p += 1 + 0
        #paper
        if (c2 == 'Y'):
            p += 2 + 3
        #scissors
        if (c2 == 'Z'):
            p += 3 + 6
    #scissors
    if (char == 'C'):
        # rock
        if (c2 == 'X'):
            p += 1 + 6
        # paper
        if (c2 == 'Y'):
            p += 2 + 0
        # scissors
        if (c2 == 'Z'):
            p += 3 + 3
print(p)
