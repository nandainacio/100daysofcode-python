glass1 = "milk"
glass2 = "juice"
print("Antes glass1:", glass1)
print("Antes glass2:", glass2)

glass3 = glass1
glass1 = glass2
glass2 = glass3

print("Depois glass1:", glass1)
print("Depois glass2:", glass2)