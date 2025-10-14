#man kann multiline strings in python folgendermaßen erstellen, indem man 3 zitatsymbole nutzt.


a = """das ist ein zitat
über mehrere zeilen
und das erkennt man auch so
cool ge?"""

print(a)

#so kannst du den buchstaben an der jeweiligen posi printen (python zählt ab 0)

print(a[2])

#ein string ist ein array, deshalb kann man durchloopen

for x in "banana":
    print(x)

#die len() funktion erlaubt die länge eines strings auszugeben

print(len(a))

#man kann checken ob ne zeichenfolge vorkommt im String, da kriegt man nen boolean raus

z = "die besten dinge sind drei"

print("drei" in z)

#man kann daraus auch if statements machen und nur printen wenn was vorhanden ist

if "drei" in z:
    print(z)

#man kann auch nach einem if not checken:

if not "zwei" in z:
    print(z)

#oder man schreibts so:

if "zwei" not in z:
    print(z)

