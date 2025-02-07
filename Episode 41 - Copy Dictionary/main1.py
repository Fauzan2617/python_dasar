dictonary = {
    "Diaz" : "Diaz Alfiari",
    "Novan" : "Novan Ramdann",
    "Hikmal" : "Hikmal Rivaldi"
}

disctionary_copy = dictonary.copy()

dictonary["Diaz"] = "DiaZ ANGJAYYY"
print(f"dicitonary {dictonary}")
print(f"dictionary_copy {disctionary_copy}")

data_hikmal = dictonary.pop("Hikmal")
print(data_hikmal)
print(dictonary)


dataend = dictonary.popitem()
print(dataend)
print(dictonary)