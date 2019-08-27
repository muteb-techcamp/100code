#week 2  ___ day9 
#learn how can we use format() method to  combine strings and numbers
# للدمج بين النصوص والارقام فإننا نستخدم دالة format
age = 34
txt= "my name is muteb, and i have{}"
print(txt.format(age))

###########################################
# يمكن تمرير عدد غير محدود من  argument  وذلك لوضعها في مكان {}
quantity=3
itemno=567
price=49.50
myorder="i want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))
######################################################
first= "muteb" ; last= "alotaibi"
full=f"{first} {last}"
print(full)
############################################
# تمرير الشقلعةثىفس للدالة باستخدام رقم الخانة في المصفوفة 
quantity=3
itemno=567
price=49.50
myorder="i want  to pay {2} dollars for {0} pices of {1} items"
print(myorder.format(quantity,itemno,price))