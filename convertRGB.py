import os.path
from PIL import Image

def getRGBColour(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def resetColour():
    return "\033[0m"

def getImagePath():
    imagePathValid = False
    while not imagePathValid:
        imagePath = input("Enter the image path to convert to ASCII...\n")
        if os.path.isfile(imagePath):
            imagePathValid = True
            print("Valid image path.")
        else:
            print("Error: Image not found")
    return imagePath

def initializeImage():
    img = Image.open(getImagePath()).convert(('RGB'))

    # Resizing image
    newWidth = 200
    width, height = img.size
    aspectRatio = height / width
    # 0.55 multiplier since characters are taller than wider
    newHeight = int(newWidth * aspectRatio * 0.55)
    img = img.resize((newWidth, newHeight))
    return img

def createASCII_RGB(img):
    asciiChars = ' .:-+*#%@'
    asciiString = ""

    for i in range(img.height):
        for j in range(img.width):
            r, g, b = img.getpixel((j, i))
            brightness = int(0.3 * r + 0.59 * g + 0.11 * b)
            # takes the min so that no matter what brightness 0-255 that it has an index
            index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
            colour = getRGBColour(r, g, b)
            asciiString += colour + asciiChars[index] + resetColour()
        asciiString += "\n"  

    print(asciiString)

def main():
    createASCII_RGB(initializeImage())

main()