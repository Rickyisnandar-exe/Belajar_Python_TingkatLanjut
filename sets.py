thissets = {"ahmad", "zaki", "muhammad" }
print(thissets)
print(type(thissets))

thissets = {"ahmad", "zaki", "muhammad", "ahmad"}
print(thissets)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, 1, 0}
print(thisset)

print(len(thisset))

print("apple" in thisset)
print("kiwi" not in thisset)

print("=====")
for x in thisset:
    print(x)

thisset.add("Ricky")
print(thisset)
print(len(thisset))

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print((thisset))
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

# thisset.remove("apple")
# print(thisset)

thisset.discard("banana")
print(thisset)
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
for x in tropical:
    print(x)

for i  in sorted(thisset):
    print(i)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print(set1 | set2)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

print(set1.union(set2,set3,set4))


set1.update(set2)
print(set1)
print(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

set1 = {"apple", 1, "banana", 0, "cherry"}
set3 = {False, "google", 1, "apple", True}
print(set3)
set4 = set1.intersection(set3)
print(set4)
print(len(set4))

himpunan1 = {1,2,3,4,5}
himpunan2 = {4,5,6,7,8}

hasil = himpunan1.difference(himpunan2)
print(hasil)
print(himpunan1 - himpunan2)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set4 = set1.symmetric_difference(set2)
print(set4)
print(set1 ^ set2)




