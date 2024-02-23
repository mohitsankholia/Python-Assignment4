value = "pacewisdom"

if len(value) < 3:
    print("Empty String")
else:
    newString = value[0:2] + value[len(value)-2:]
    print(newString)