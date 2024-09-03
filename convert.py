import convertGreyscale
import convertRGB

def main():
    inputValidFlag = False
    while not inputValidFlag:
        colourOption = input("Would you like the ASCII image in RGB? (y/n)...\n")
        if (colourOption.lower() == "y"):
            # run the convertRGB.py
            inputValidFlag = True
        elif (colourOption.lower() == "n"):
            # run the convertGreyscale.py
            inputValidFlag = True
        else:
            print("Invalid Input: Try again")
