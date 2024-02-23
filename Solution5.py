firstString = "abc"
secondString = "xyz"

print(firstString.replace(firstString[0:2], secondString[0:2]))

print(secondString.replace(secondString[0:2], firstString[0:2]))