import os.path
from PIL import Image

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
    img = Image.open(getImagePath()).convert('L')

    # Resizing the image
    newWidth = 500
    width, height = img.size
    aspectRatio = height / width
    # 0.55 multiplier since characters are taller than wider
    newHeight = int(newWidth * aspectRatio * 0.55)
    img = img.resize((newWidth, newHeight))
    return img

def create_ASCII_Greyscale(img):
    asciiChars = ' .:-+*#%@'
    asciiString = ""

    for i in range(img.height):
        for j in range(img.width):
            brightness = img.getpixel((j, i))
            # takes the min so that no matter what brightness 0-255 that it has an index
            index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
            asciiString += asciiChars[index]
        asciiString += "\n"  

    print(asciiString)

def run():
    create_ASCII_Greyscale(initializeImage())

run()

