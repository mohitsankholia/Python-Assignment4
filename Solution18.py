value = "32.054,23"

tempValue = value.replace(".", "_")
midValue = tempValue.replace(",", ".")
resultValue = midValue.replace("_", ",")

print(resultValue)
