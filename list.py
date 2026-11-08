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

# print(thislist)

# thislist.remove("mango")
# print(thislist)

# thislist.pop(1)
# print(thislist)

# del thislist[0]
# print(thislist)

# thislist.clear()
# print(thislist)

# del thislist

# print(thislist)

for x in thislist:
    print(x)

for x in range(len(thislist)):
    print(x)


iniBuah =  ["apple", "banana", "cherry", "kiwi", "mango"]

listBaru = [x for x in iniBuah if "a" in x]
print(listBaru)


thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

listSaya = thislist.copy()
print(listSaya)

listSaya1 = list(thislist)
print(listSaya1)

listBaruKemarin = thislist [1 : 3]
print(listBaruKemarin)


list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

list_baru = list1 + list2
print(list_baru)

list1.extend(list2)
print(list1)

for x in list2:
    list1.append(x)
    print(list1)