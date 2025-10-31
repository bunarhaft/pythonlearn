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

y = 0

print(f"Es steht folgendes in variable x: {x} ")
print(bool(x))

print(f"Es steht folgendes in variable y: {y}")
print(bool(y))

#false ist alles was leer ist und was 0 nicht

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#wert btw objekt in diesem fall ist false, wenn es eine funktion gibt die 0 zurückgibt

print("wert btw objekt in diesem fall ist false, wenn es eine funktion gibt die 0 zurückgibt")

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#funktionen können nen boolean returnn

print("gibt true aus")
def myFunction() :
    return True


print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")