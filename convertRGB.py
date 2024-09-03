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

def getImageWidth(imagePath):
    img = getImage(imagePath)

    originalWidth = img.size[0]
    newWidth = 0

    isValidWidth = False

    while not isValidWidth:
        try:
            widthOption = int(input("How wide should the ASCII image be? (px)...\n"))
            if (widthOption <= originalWidth and widthOption > 0):
                newWidth = widthOption
                isValidWidth = True
            else:
                print("Try again. Width can't be greater than original image.")
        except:
            print("Try again. Enter a valid integer number of pixels.")

    return newWidth

def getImage(imagePath):
    img = Image.open(imagePath).convert('RGB')
    return img

def resizeImage(img, userWidth):
    # Resizing image
    newWidth = userWidth
    width, height = img.size
    aspectRatio = height / width

    # 0.55 multiplier since characters are taller than wider
    newHeight = int(newWidth * aspectRatio * 0.55)
    img = img.resize((newWidth, newHeight))

    return img

def create_ASCII_RGB(img):
    asciiChars = ' .:-+*#%@'
    asciiString = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            brightness = int(0.3 * r + 0.59 * g + 0.11 * b)
            # takes the min so that no matter what brightness 0-255 always has an index
            index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
            colour = getRGBColour(r, g, b)
            asciiString += colour + asciiChars[index] + resetColour()
        asciiString += "\n"  

    print(asciiString)

def run():
    imagePath = getImagePath()
    image = getImage(imagePath)
    newWidth = getImageWidth(imagePath)
    resizedImage = resizeImage(image, newWidth)
    create_ASCII_RGB(resizedImage)

run()