#Set methods

#add()
"add an element in the list"
list1={1,2,3,4}
list1.add(5)
print(list1)

output={1,2,3,4,5}
#clear()
"removes all the elements from the list"
list1={1,2,3,4,5}
list1.clear()
print(list1)

output={}
#copy()
"returns a copy of the list"
list1={1,2,3,4,5}
list1.copy()
print(list1)

output={1,2,3,4,5}
#differance()
"returns a set containing the differance between two or more"
list1={1,2,3,4}
list2={3,4,5,6,7}
list3=list1.difference(list2)
print(list3)

output={1,2}
