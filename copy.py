#deep copy

a=[2,5,3,7,8]
b=a.copy()
a[2]=9
print(a)
print(b)



#direct copy

list=[1,2,3,4,5,6]
b=list
list[1]=10
print(b)
print(list)
