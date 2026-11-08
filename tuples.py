thisTuple = ("banana", "jagung", "makroni", "aple", "ahmad" , "mapel", "matkul")
tupeLagi = "ayah", "ibu", "kakak"
print(thisTuple)
print(tupeLagi)
print(len(thisTuple))
print(type(tupeLagi))

print(thisTuple[1])
print(thisTuple[-2])
print(thisTuple[0:2])
print(thisTuple[-3 : -1])
print(thisTuple[:4])
print(thisTuple[2:])

print("ahmad" in thisTuple)
print("jagung" not in thisTuple)

y = list(thisTuple)
print(y)

# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# y.append("banana")
# x = tuple(y)
# print(x)

y = ("kucing", "ayam", "mangga")
thisTuple += y
print(type(thisTuple))
print(thisTuple)

y = list(thisTuple)
y.remove("ayam")
print(y)

thisTuple = tuple(y)
print(thisTuple)

# del thisTuple
# print(thisTuple)

matkul = ("aij", "pemograman", "arkom", "basisdata", "apple", "banana", "cherry", "strawberry", "raspberry")

(x, y, z, a, *b) = matkul

print(matkul)
print(x)
print(y)
print(a)
print(b)

data = ("budi", 18, "bekasi")
(x, _, y) = data
print(x, y)


for x in thisTuple:
    print(x)

for x in range(len(thisTuple)):
    print(x)

i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1

for i, buah in enumerate(thisTuple):
    print(i, buah)

for i, buah in enumerate(thisTuple, start=1):
    print(f"{i}. {buah}")

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
mytuple = tuple1 + tuple2
print(mytuple)

a = (1, 2)
b = (3, 4)
c = (5,)
print( a + b + c )

fruits = ("apple", "banana", "cherry")
buahBanyak = fruits * 2
print(buahBanyak)

t = buahBanyak + ("kiwi" ,)
print(t)


