#week4 ____ day20
#A set is a collection which is unordered and unindexed.
# create Empty set
thisset={}
print(thisset)
#=====================================================
print("please create a new st and assign it ")
myset={"apple","galaxy","htc"}
print(myset)
#====================================================
print("set is not contain aduplicated value & unorderd")
myset={20,15,20,"apple","galaxy","htc","htc"}
print(myset)
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print("You cannot access items in a set by referring to an index, since sets are unordered the items has no index but by using Loop through the set and print the values")
myset1={"apple","banana","orange","cherry"}
for x in myset1:
 print(x)
 print("apple" in myset1) # the result will be true.
 #++++++++++++++++++++++++++++++++++++++++++++++++++++++
 #Once a set is created, you cannot change its items, but you can add new items
 print("To add one item to a set use the add() method")
 myset2={"apple","banana","orange","cherry"}
 myset2.add("struberry")  #لا تقبل سوى عنصر واحد في كل مرة. add()
 print(myset2)

#=====================================================

 print("Add multiple items to a set, using the update() method. ")
 myset3={"muteb","turki","yasser"}
 myset3.update(["sultan","fahad","saif"])
 print(myset3)
 