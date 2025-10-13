#variablen die außerhalb einer funktion erstellt werden sind global und können überall benutzt werden

x = "stramm"

def myfunc():
    print("Python ist " + x)


myfunc()

#Wenn man ne Variable innerhalb einer funktion deklariert, ändert sie ihren Wert nur lokal innerhalb der funktion

y = "stabil"

def myfunc(): 
    y = "test"
    print("Python ist " + y)


myfunc()

print("Python is " + y)

#Mit global kann man definieren dass eine variable global definiert wird innerhalb einer funktion
def myfunc():
    global y
    y = "echt cool"

myfunc()

print("Python ist " + y)

# um eine änderung einer bereits vorhanden variable global zu machen, benötigt man ebenso den global tag

z = "super!"

def myfunc():
    global z
    z = "mega cool"

myfunc()

print("Python ist: " + z)