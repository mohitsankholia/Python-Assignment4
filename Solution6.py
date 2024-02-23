firstString = "abc"
secondString = "string"

if secondString.endswith("ing"):
    newString = secondString + "ly"
else:
    newString = secondString + "ing"

print(newString)
