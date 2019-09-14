#week4 ____ day 24 
# use the built-in Dictionary method copy(). لنسخ القاموس الى قاموس اخر نستخد  الدالة copy()
my_dict ={
    "name":"muteb",
    "f_name":"alotaib",
    "age":34
}
this_dict=my_dict.copy()
print(this_dict)
#Another way to make a copy is to use the built-in method dict() :
this_dict=dict(my_dict)
print(this_dict)
#+++++++++++++++++++++++++++++++++
#A dictionary can also contain many dictionaries, this is called nested dictionaries. 
#Create a dictionary that contain three dictionaries
familydict={
"father":{
      "name":"turki",
        "age":45
        },
        "muther":{
            "name":"eman",
            "age":34
        },
        " chaild" :{
             "name":"yazeed",
             "age":2
         }
}
print(familydict)
#+++++++++++++++++++++++++++++++++++++++++++++++
#use the dict() constructor to make a new dictionary:
this_dict= dict("name"="muteb" , "gender"="male" , "age"=34)
print(this_dict)