cars = ["mobil1", "mobil2", "mobil"]
baru = cars[0]
print(baru)

ubah = cars[1] = "toyota"
print(cars)
print(len(cars))

cars.append("innnov")
cars.insert(1, "mobil3")
cars.sort()
print(cars)
print(len(cars))
cars.reverse()
print(cars)
cars.pop(1)
print(cars)
cars.remove("innnov")
print(cars)


