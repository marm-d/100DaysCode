thistuple = ("apple","banana","charry")
if "apple" in thistuple:
    print("Yes, 'apple' is in fruits tuple")

thistuple = ("بايثون",) * 3
print(thistuple)

thistuple = ("بايثون") * 3
print(thistuple)

thistuple1 = (1,2,3,4)
thistuple2 = (5,6)

thistuple = thistuple1 + thistuple2

print(thistuple)

x = (3,4,5,6)
x = x + (1,2,3)
print(x)

thistuple = ("apple","banana","charry")

print(len(thistuple))


thistuple = tuple(("apple","banana","charry"))
print(thistuple)


thislist = [3,4,5,6,"A","B"]
thistuple = tuple(thislist)
print(thistuple)