mydict = dict( name = "Liya", age = 20, course = "3rd")
print(mydict)
print(type(mydict["name"]))
Year = mydict.get("age")
print(Year)
mydict["Faculty"] = "SITE"
print(mydict)
a = mydict.keys()
b = mydict.values()
print(a)
print(b)
if "age" in mydict:
    print("It's here")
else: 
    print("There's no such word")