#week2 -- day11
# logical operators in python:
# using  and & or operators  in this example:
x=5
print(x>3 or x<4 ) # return true becouse one of condition are true.
print(x<10 and x>4) # return true becouse both of condition are true.
################################
# python identity operators 
# يستخدم العامل isللمقارنة بين متغيرين والتاكد من كونها يشيران الى (كائن واحد) ولهما نفس المكان في الذاكرة
x=["apple" , "banana"] 
y=["apple" , "banana"]
z=x
print(x is not z) # return false becouse x and z the same ( we are assign z=x)
print(x is not y) # return true becouse x and y is not the same object in the memory
print(x != y)     #return false becouse  x=y
#############################
# المعامل in and not in تستخدم لمعرفة ان كانت المصفوفة تحتوي على القيمة المدخلة أم لا
x=['apple','orange','banana']
print('orange' in x)
print("banana" in x)