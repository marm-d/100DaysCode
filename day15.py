thislist = ["apple","banana","charry"]
print(len(thislist))

thislist.append("orangr")
print(thislist)

thislist = ["apple","banana","charry"]
thislist.insert(1,"orangr")
print(thislist)

thislist = ["apple","banana","charry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple","banana","charry"]
thislist.pop()
print(thislist)


thislist = ["apple","banana","charry"]
thislist.pop(1)
print(thislist)

print()

thislist = ["apple","banana","charry"]
thislist.clear()
print(thislist)

print()

thislist = ["apple","banana","charry"]
mylist = thislist.copy()
print(mylist)

print()

thislist = ["Omar","Majed","Naif"]
mylist = thislist.copy()
thislist.pop(0)
print(mylist)
print(thislist)

print()

thislist = ["Omar","Majed","Naif"]
mylist = thislist
thislist.pop(0)
print(mylist)
print(thislist)

print()

thislist = ["apple","banana","charry"]
mylist = list(thislist)
print(mylist)

print()

thislist = list(("apple","banana","charry"))
print(thislist)

print()