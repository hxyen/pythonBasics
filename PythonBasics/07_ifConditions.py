# write a weight converter (kg, lbs)
weight = float(input("Weight: "))
weightUnit = input("Enter 'k' for kg or 'l' for Lbs: ")

try:
    if weightUnit == "k":
        print("Weight in Lbs: " + str(weight*2.20462))
    elif weightUnit == "l":
        print("Weight in Kg: " + str(weight/2.20462))
    else:
        print("You can only enter 'k' or 'l' for the weight unit! Please try again.")
    # If you want to ignore if it's big "K" or small "k" then use the operator weightUnit.upper()=="K" OR weightUnit.lower()=="k"

except ValueError:
    print("You can only type in numbers for your weight! Please try again.")
