#week2 -- day12 
# print  after make a changer :
s= "please ,I want {} sandwishes and {} donutes " # assign this sentence to a variable S
# 1-change i to we by using replace() method:
print (s.replace("I","We")) 

# 2- fill the space by using the format method
sandwish_no=5
donuts_no=7
b=s.format(sandwish_no,donuts_no)
print(b)
# 3- convert every a letters from lower case to upper case :
print(b.replace('a','A'))