#man kann in python mehrere variablen in einer reihe deklarieren

x, y, z = "hallo", "test", 1

print(x)
print(y)
print(z)

#man kann denselben wert auf mehrere variablen geben

x = y = z = "ein gleicher Wert"

print(x)
print(y)
print(z)

#ne liste kann man ebenso in variablen einpacken

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)