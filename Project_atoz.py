print("Letter 'a'")
print()
for row in range(4):
    for col in range(5):
        if (row==0 and col%3!=0 and col!=4) or (row==1 and col%3==0) or (row==2 and col%3==0) or (row==3 and col%3!=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'b'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==0) or (row==2 and col>=0) or (row==3 and col%3==0) or (row==4 and col>=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'c'")
print()
for row in range(5):
    for col in range(4):
        if (row==0 and col>0) or (0<row<4 and col==0) or (row==4 and col>0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'd'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==3) or (row==2 and col>=0) or (row==4 and col>=0) or (row==3 and col==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'e'")
print()
for row in range(5):
    for col in range(4):
        if (col!=1 and row==2) or (0<row<4 and col==0) or ((row==0 or row==4)  and col>0) or (row==1 and col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'f'")
print()
for row in range(5):
    for col in range(4):
        if (row>0 and col==1) or (row==2 and col>=0) or (row==0 and col>1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'g'")
print()
for row in range(5):
    for col in range(4):
        if ((row==2 or row==4) and col>=0) or (row>0 and col==3) or (row==0 and col%3!=0) or (row==1 and col==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

print("Letter 'h'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==0) or (row==2 and col>=0) or (col==3 and row>1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'i'")
print()
for row in range(5):
    for col in range(4):
        if (col==2 and row!=1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'j'")
print()
for row in range(5):
    for col in range(4):
        if (col==2 and row!=1) or (row==4 and col==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'k'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==0) or ((row==1 or row==3) and col==1) or ((row==0 or row==4) and col==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'l'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'm'")
print()
for row in range(5):
    for col in range(5):
        if (row>0 and (col==0 or col==2 or col==4)) or (row==0 and(col==1 or col==3)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'n'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==0) or (row>0 and col==3) or (row==1 and col==1) or (row==0 and col==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'o'")
print()
for row in range(4):
    for col in range(4):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row==2 and col%3==0) or (row==3 and col%3!=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'p'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==0) or ((row==0 or row==2) and col>=0) or (row==1 and col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'q'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==3) or ((row==0 or row==2) and col>=0) or (row==1 and col==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'r'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==1) or (row==0 and col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 's'")
print()
for row in range(5):
    for col in range(4):
        if (row==0 and col>0) or (row==1 and col==0) or (row==2 and col%3!=0) or (row==3 and col==3) or (row==4 and col<3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 't'")
print()
for row in range(5):
    for col in range(4):
        if (row>=0 and col==1) or (row==1 and col<3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'u'")
print()
for row in range(5):
    for col in range(4):
        if (row<4 and (col==0 or col==3)) or (row==4 and col%3!=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'v'")
print()
for row in range(5):
    for col in range(4):
        if (row<4 and (col==0 or col==3)) or (row==4 and col==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'w'")
print()
for row in range(5):
    for col in range(5):
        if (row<4 and (col==0 or col==4)) or (row==4 and (col==1 or col==3)) or ((row==2 or row==3) and col==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'x'")
print()
for row in range(5):
    for col in range(5):
        if ((row==0 or row==4) and (col==0 or col==4)) or ((row==1 or row==3) and (col==1 or col==3)) or (row==2 and col==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'y'")
print()
for row in range(5):
    for col in range(5):
        if (row==0 and (col==0 or col==4)) or (row==1 and (col==1 or col==3)) or (row==2 and col==2) or (row==3 and col==1) or (row==4 and col==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
print("Letter 'z'")
print()
for row in range(4):
    for col in range(4):
        if ((row==0 or row==3) and col>=0) or (row==1 and col==2) or (row==2 and col==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
