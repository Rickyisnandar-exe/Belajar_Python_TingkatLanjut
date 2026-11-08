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
