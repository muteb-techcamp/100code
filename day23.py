#week4 __ day23 
# To determine if a specified key is present in a dictionary use the in keyword:
my_dict ={
    "name":"muteb",
    "f_name":"alotaib",
    "age":34
}
print(my_dict)
if "f_name" in my_dict:
 print("yes 'f_name'  is one of key on the my_dict dictionary")
#+++++++++++++++++++++++++++++
#To determine how many items (key-value pairs) a dictionary has, use the len() method:
thisdict={
    "brand":"ford",
    "model":"mustang",
    "years":2008
}
print(len(thisdict))
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"]="red"
print(thisdict)
#There are several methods to remove items from a dictionary:
thisdict.pop("model") #The pop() method removes the item with the specified key name. 
print(thisdict)
thisdict.popitem() #to remove the last items from dictionary:
print(thisdict)
del thisdict["years"]
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict