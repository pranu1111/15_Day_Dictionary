mydict = {
    
    "name" : "Pranita",
    "Dob": 10011994,
    "color" : "fair",
    "name" : "Pranita",
    "age"  : 27,
}
# print(mydict,type(mydict))
# print(mydict["name"])
# print(mydict["Dob"])
# print(mydict["color"])

# print(mydict)
# print(mydict["Dob"])
# print(mydict.get("color"))
# print(mydict.get("name"))
# print(mydict.get("age"))
# z=mydict.keys()
# print(z)
 
mydict["contact"]=1235996

# print(mydict)

# dict={
    
#     "model": "verna"
    
# }

# dict["no"]=123456
# dict["color"]="white"
# dict["version"]=1556
# dict["mfc"]=12102000
# dict["valid"]=1212025

# # print(dict)

# dict["color"]="black"
# print(dict)

# mydict.pop("contact")
# print(mydict)

# mydict.popitem()
# print(mydict)

# del mydict["age"]
# print(mydict)

# del mydict
# print(mydict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# # print(thisdict)
# for x in mydict:print(x)

# tisidict={
#     "color" : "red",
#     "range": 123456,
#     "id": 1589
    
# }

# mydict=tisidict.copy()
# print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# mydict = dict(thisdict)
# print(mydict)

dict = {
  "child1":{
    
    "name" : "p",
    "id" :12345,
    "class" : "BE IT",
    "year"  : "1st"
    },
  "child2":{
    
    "name" : "s",
    "id" :45121,
    "class" : "BE IT",
    "year"  : "2st"
    
  },
  
  "child3":{
    
    "name" : "c",
    "id" :98541,
    "class" : "BE IT",
    "year"  : "3st"
  }
}
# print(dict)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# print(myfamily)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

# print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x=car.copy()

print(x)