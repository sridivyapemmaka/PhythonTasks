
#print A

str=""
for row in range(0,7):
    for col in range(0,5):
        if((col== 0 or col== 4) and row!=0) or ((row== 0 or row== 3) and(col> 0 and col<4)):
            str=str+"*"
        else:
            str=str+" "
        
    str=str+"\n"
    
print(str)

#print B
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or (col== 4 and(row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and(col>0 and col<4)):
            str=str+"*"
        else:
            str=str+" "
    str=str+"\n"
print(str)

#print C
str=""
for row in range(0,7):
    for col in range(0,5):
        if (col==0 and (row!=0 and row!=6))or ((row==0 or row==6) and (col>0)):
            str=str+" *"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print D

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or  row==6) and (col>0 and col<4)):
              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)
            
#print E

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or ((row==0 or row==3 or row==6) and (col>0)):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print F

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or ((row==0 or row==3 ) and (col>0)):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)           

#print G
str=""
for row in range(0,7):
    for col in range(0,6):
        if(col==0)or (col==4 and (row!=1 and row!=2)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==3 and (col==3 or col==5)):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)          

#print H

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0 or col==4) or (row==3):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)      

#print I

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==2) or (row==0 or row==6) and( col!=2):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str) 

#print J
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==2) or( row==0 and col!=2) or (row==6 and col<2):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print K
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or (col+row==4 or row-col==2):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str) 
#print L

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0 or row==6):

              str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print M

str=""
for row in range(0,7):
    for col in range(0,7):
        if(col==0 or col==6) or (( row == col) and (col>0 and col < 4)) or (row==1 and col==5) or (row==2 and col==4):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str) 

#print N

str=""
for row in range(0,7):
    for col in range(0,7):
        if(col==0 or col==6) or ((row==col )and (col>0 and col<6)):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str) 
#print O
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0 or col==4) and  (row!=0 and row!=6)or ((row==0 or row==6) and (col>0 and col<4)) :
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)
#print P

str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0) or( col==4 and (row ==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)) :
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print Q

str=""
for row in range(0,8):
    for col in range(0,5):
        if((col==0 or col==4) and (row>0  and row<6)) or ((row==0 or row==6) and(col>0 and col<4))or ((row==5 and col==1) or (row==7 and col==3)):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print R
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==0)or(col==4 and(row!=0 and row!=3))or((row==0 or row==3)and  (col>0 and col<4)) :
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print S
str=""
for row in range(0,7):
    for col in range(0,7):
        if((row==0 or row==3 or row==6) and col>1 and col<5) or ((col==1 and (row==1 or row==2 or row==6)) or (col==5 and (row==0 or row==4 or row==5))):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print T
str=""
for row in range(0,7):
    for col in range(0,5):
        if(col==2) or ( row== 0 and col!=2) :
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print U

str=""
for row in range(0,7):
    for col in range(0,5):
        if((col==0 or col==4) and row!=6) or (row==6 and (col>0 and col<4)):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

#print V

str=""
for row in range(0,4):
    for col in range(0,7):
        if(row==col)or (row+col==6):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)

 #print W

str=""
for row in range(0,4):
    for col in range(0,6):
        if(col==0 or col==5)or( row+col==3)or (col-row==3):
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)
'''
#print X

str=""
for row in range(0,4):
    for col in range(0,6):
        if(row
           str=str+"*"
        else:
            str=str+" " 
    str=str+"\n"
print(str)'''



        

























