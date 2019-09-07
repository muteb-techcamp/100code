#week 3 __  day17 
#to check if ilems is exist or not :
tuple_info=("orange","apple","cherry")
if 'apple' in tuple_info :
    print("yes, apple is in the fruits tuple")
#+++++++++++++++++++++++++++
# to raplecate the items  we will use  * opreators:
thistuple =("muteb",)*3
print(thistuple)
thistuple =("muteb")*3
print(thistuple)
#+++++++++++++++++++++++++
#To add 2 tuples or more into one tuple
thistuple1=(10,20,30,40)
thistuple2=(15,25,35,45)
thistuple=thistuple1+thistuple2
print(thistuple)

x=(1,2,3,5)
x=x+(7,9)
print(x)
#To determine how many items a tuple has, use the len() method
thistuple=(10,20,30,40,50,60)
print(len(thistuple))
#+++++++++++++++++++++++++++++
#Using a tuple() method to make thetuple 
this_tuple=tuple(('arar','skaka',"tabuk"))
print(this_tuple)
#++++++++++++++++++++++++++++
# to convert  items of list to items in tuple

thelist=['arar','skaka',"tabuk",40,40,'a','b','a']
thetuple=tuple(thelist)
print(thetuple)

