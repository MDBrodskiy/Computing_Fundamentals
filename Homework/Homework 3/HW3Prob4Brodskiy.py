"""
 * ===============================================================
 *
 *       Filename:  HW3Prob4Brodskiy.py
 *       Assignment: Homework 3 Problem 4
 *       Title: String metric to imperial converter
 *
 *    Description:  Performs metric to imperial conversion
                    from string phrases
 *
 *        Version:  1.0
 *        Created:  03/21/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

def stringCalc(phrase):

    modifiers = {"kilo":.001, "hecto":.01, "deka":.1, "":1, "deci":10, "centi":100, "milli":1000}
    units = ["meter", "meters", "gram", "grams", "liter", "liters", "foot", "feet", "pound", "pounds", "gallon", "gallons"] 
    factors = [.3048, .3048, 453.59, 453.59, 4.546, 4.546, 3.28, 3.28, .0022, .0022, .22, .22]
    tokens = phrase.lower().replace("?","").split()
    initialBaseUnit = ""
    initialUnit = ""
    initialQuant = 0
    initialModifier = ""
    finalBaseUnit = ""
    finalUnit = ""
    finalModifier = ""
    unitListLength = len(units)

    for i in tokens:
        for j in modifiers.keys():
            for k in range(unitListLength):
                if (i == (j + units[k]) and finalUnit == ""):
                    finalBaseUnit = units[k]
                    finalUnit = i
                    finalModifier = j
                elif (i == (j + units[k])):
                    initialBaseUnit = units[k]
                    initialUnit = i
                    initialModifier = j

    if (abs(units.index(finalBaseUnit) - units.index(initialBaseUnit)) % 5 == 0):
        initialQuant = 1.0
    elif (abs(units.index(finalBaseUnit) - units.index(initialBaseUnit)) % 6 == 0): 
        initialQuant = float(tokens[tokens.index(initialUnit) - 1])
    else:
        print("The conversion from", initialUnit, "to", finalUnit, "is invalid. Exiting...")
        return "Error!"

    return f"There are {modifiers[finalModifier] * initialQuant * factors[units.index(finalBaseUnit)] / modifiers[initialModifier]:.4f} {finalUnit} in {initialQuant} {initialUnit}"

print("Enter a conversion phrase below.")
print("Prefixes from milli- to kilo- are valid.")
print(stringCalc(input("Available units include meters/feet, grams/pounds, and liters/gallons:  ")))
