word = "restart"
firstWord = word[0]

newString = firstWord + word[1:].replace(firstWord, "$")

print(newString)
