#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple
t1=("Java","Python", "SQL", "C" )
print(t1)
#2. Write a python program to store only one item using tuple.
t2="Hellow"
print(t2)
#3. Write a python program to reverse the tuple.
t2="Hellow"
print(t2[::-1])
#4. Write a python program to Swap two tuples in Python.
t1=("Java","Python", "SQL", "C" )
t2="Hellow"
t1,t2=t2,t1
print("t1=",t1,"\nt2=",t2)
#5. Write a python program to check if all items in the tuple are the same.
tuple1=(100, 200, 300, 400)
b=all(i==tuple1[0] for i in tuple1)
if(b):
    print("Equal")
else:
    print("Not Equal") 
#6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)
tuple1=(100, 200, 300, 400)
t2,t3,t4,t5=tuple1
print(t2,t3,t4,t5,type(t2))
#7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
tuple1=(1,2,3,4,5,6)
c_tuple=tuple1[3:5]
print("New tuple=",c_tuple)
#8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
b=list(tuple1)
b.sort(key= lambda iteam:iteam[1])
print("New tuple base on 2nd element ",tuple(b))
#9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])
#10. Write a python program to change the first item (22) of a list within the following tuple to 222. tuple1 = (11,[22,33],44,55)
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)