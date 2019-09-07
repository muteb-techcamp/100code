# week3 __ day15
#To determine how many items of index has, use the len() method. 
list_of = ["apple","banana","orange","cherry"]
print(len(list_of))
 #+++++++++++++++++++++++++++++
 # to add a new elemnent in end of index we use the append() method.
mylist=["apple","banana","orange","cherry"]
mylist.append("stroberry")
print(mylist)
#+++++++++++++++++++++++++++++
# to add a new elemnent in any location in index use the insert() method.
name_student=["muteb","yazan","yzeed"]
name_student.insert(1,"fahad")
print(name_student)
#++++++++++++++++++++++++++++++++
# to remove by using remove() mothed:
student_inf=['name',"age",id]
student_inf.remove(id)
print(student_inf)
#+++++++++++++++++++++++++++++++
#The pop() method to  removes the specified index by give it a prametere anumber of index
element_list=["muteb","yazan","turki",1500]
element_list.pop(2)
print(element_list)
element_list.pop()
print(element_list)
#++++++++++++++++++++++++++++++++++++++++++++
# using The clear() method to  empties the list.
city=['riyadh','jeddah',"makkah","taif","khober"]
city.clear()
print(city)
#++++++++++++++++++++++++++++++++++++
# to make a copy from list we are using copy() method:
city=['riyadh','jeddah',"makkah","taif","khober"]
name_city=city.copy()
print(name_city)
name_city.pop(3)
print(name_city)
city=name_city
print(city)
#++++++++++++++++++++++++++++++++
 #make a copy is to use the built-in method list(). 

city=['riyadh','jeddah',"makkah","taif","khober"]
city_n=list(city)
print(city_n)

#+++++++++++++++++++++++++++++++++++
#Using the list() constructor to make a list

thislist=list(("orange","apple","banana","cherry"))
print(thislist)