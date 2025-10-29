#die upper() methode bringt den string in großschrift zurück

a = "Hello, World! aber groß!"

print(a.upper())

#die lower() methode bringt den string in kleinschrift zurück

b = a.upper() + " spaß klein"

print(b.lower())

#die strip() methode entfernt leerzeichen am ende und anfang

c = " leerzeichen, siehst du gibts keine? "

d = "   aber hier gibts welche am anfang guckst du   "

print (c.strip())

print (d)

#replace methode replaced sachen

print(a.replace("H", "J"))

#Split() splittet den string an den jeweiligen instanzen eines seperator

e = "Hello, World!"

print(e.split(",")) 
