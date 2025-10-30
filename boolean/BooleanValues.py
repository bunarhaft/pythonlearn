#man muss wissen ob ne expression true oder false ist

#bei booleans kriegt man jeweils eines von beiden

print(10 > 9)

print(10 == 9)

print(10 < 9)

a = 200

b = 33

if b > a:
    print("b is größer als a")

else:
    print("b is nicht größer als a")


#man kann jeden Wert evaluieren

#True weil String hat Inhalt
print(bool("Hello"))

#False weil kein Inhalt im String ist
print(bool(""))

#selbes beispiel
print(bool(15))

print(bool())

x = "allo"

y = ""

print("Es steht folgendes in variable x: {x} ")
print(bool(x))

print("Es steht folgendes in variable y: {y}")
print(bool(y))

