inputString = input("Enter String : ")

if len(inputString) % 4 == 0:
    print(inputString[:: -1])

else:
    print(inputString)