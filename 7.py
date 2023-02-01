mydict = dict( name = "Liya", age = 20, course = "3rd")
print(mydict["course"])
mydict.update({"age":2020})
print(mydict)
if "Liya" in mydict:
    print("It's here")
else: 
    print("There's no such word")
if "name" in mydict:
    print("It's here")
else: 
    print("There's no such word")
mydict["age"] = 21
print(mydict)