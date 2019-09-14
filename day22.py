#week 4 ___ day22 : Dictionaries :-
#A dictionary is a collection which is unordered, changeable and indexed.  
#dictionry={key : value}
print("show us your car informationd:")
thisdict={"brand":"ford", "model": "mustang" ,"year":1978}
print(thisdict)
#+++++++++++++++++++++++++++++
#You can access the items of a dictionary by referring to its key name:
thisdict={
    "name":"muteb",
    "gender":"male",
    "age":33
    }
x=thisdict["name"]
print(x)
#+++++++++++++++++++++++++++++++++++++++
#You can change the value of a specific item by referring to its key name. 
thisdict={
    "name":"muteb",
    "gender":"male",
    "age":33
    }
thisdict["age"]=25
print(thisdict)

#You can loop through a dictionary by using a for loop
my_info={"name":"muteb", "gender":"male", "age":33 }
for x in my_info:
 print(my_info[x])
 #use the values() function to return values of a dictionary
for x in thisdict.values():
 print(x) 
 #+++++++++++++++++++++++++
 #Loop through both keys and values, by using the items() function
 my_info={
     "name :":"muteb",
  "gender :":"male",
   "age :":33 
   }
for x,y in my_info.items():
  print(x,y)