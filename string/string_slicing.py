#man kann eine reichweite an charactern returnen mit der slice syntax

#man holt sich alle characters von 3 - 6 (ohne den letzten zu inkludieren)
b = "hallo biro"
print(b[3:6])

#bei 6 : 10 bekäme man Biro

print(b[6:10])

#wenn man keinen start index angibt wird von anfang an gesliced

print(b[:5])

#beim löschen des end index sliced man von anfang des index bis zum ende

print(b[6:])

#man kann mit negativ indexen arbeiten um den slice vom ende des strings zu starten

print(b[-5: 7])
