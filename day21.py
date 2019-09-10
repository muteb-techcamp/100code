#week 4 __ day21 
#To determine how many items a set has, use the len() method:
print("To determine how many items a set has, use the len() method")
set_me={"muteb","turki","yazan","fahad"}
print("length os myset is:",len(set_me))
#=======================================
#To remove an item in a set, use the remove(), or the discard() method
print("Remove 'turki' by using the remove() method.")
set_me.remove("turki")
print(set_me)
#note: If the item to remove does not exist, remove() will raise an error!.
print("Remove 'fahad' by using the discard() method")
set_me.discard('fahad')
print(set_me) 
######################################
set1={"apple","srtuberry","banana","cherry","orange","mango"}
x=set1.pop()
print(x)
print(set1)
set1.clear()
print(set1)
set2={"apple","srtuberry"}
del set2
print(set2)
#+++++++++++++++++++++++++++++++++++
#Using the set() constructor to make a set.
print("build a new set for corporation of cars:")
thisset=set(("ford","toyota","chevroleh"))
print(thisset)
