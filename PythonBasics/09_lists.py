azubis = ["Fabian", "Linus", "Sebastian", "Philip", "Huyen"]
azubis[4] = "Ich"  # or azubi[-1] = "Ich"
print(azubis[0:3])
print(azubis)


# list methods
azubis.append("newAzubi1")
azubis.insert(-1, "newAzubi2")
print(azubis)

azubis.remove("newAzubi2")
print(azubis)

# number of elements(here: Azubis) in the list with len-function
print(len(azubis))

# searching if a specific element is in the list
print("Linus" in azubis)

azubis.clear()
print(azubis)
