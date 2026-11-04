myList = ["apple", "Banana", "Pinaple"]
myList1 = [1, 2, 3, 4, 5]
myList2 = [True, False, True]
campur = ['apple', 2, 30, False]
print(myList)

print(myList[0])
print(myList[-1])
print(len(myList))

print(myList1)
print(myList2)
print(campur)


print(type(campur))

ubah_kelist = list(("apple", "banana", "cherry"))
print(ubah_kelist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:4])
print(thislist[:4])
print(thislist[2:])
print(thislist[-5:-2])
print(thislist[-6:-4])


thislist[1] = "pisang"
print(thislist)


thislist[1:3] = ["banana", "watermelon", "melon"]
print(thislist)

thislist.insert(2, "Blackmamba")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("Coco")
print(thislist)

thislist.insert(2,"bananaThecoco")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

print(thislist)



