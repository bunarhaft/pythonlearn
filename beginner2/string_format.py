#man kann strings und nummern mit F-Strings oder format() methode verbinden

age = 36
txt = f"ich bin irfan, ich bin {age} jahre alt"

print(txt)

#bei geschweiften klammern hat man einen platzhalter

price = 59
txt = f"der Preis ist {price} Evro"
print(txt)

#ein platzhalter kann einen modifier haben um den value zu formatieren. man fügt nen modifier mit nem : hinzu. beispielweise :.2f um einen float format zu haben

price = 59

txt = f"Der Preis ist {price:.2f} dollars"
print(txt)

#ein platzhalter kann Pythoncode beinhalten, wie bspw eine mathe operation

txt =f"Der Preis ist {20 * 59} Evro"

print(txt)