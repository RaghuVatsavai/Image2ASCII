import os.path
from PIL import Image, ImageFont, ImageDraw

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
    img = Image.open(imagePath).convert('L')
    return img

def resizeImage(img, userWidth):
    # Resizing the image
    newWidth = userWidth
    width, height = img.size
    aspectRatio = height / width
    # 0.55 multiplier since characters are taller than wider
    newHeight = int(newWidth * aspectRatio * 0.55)
    img = img.resize((newWidth, newHeight))
    return img

def create_ASCII_Greyscale(img):
    asciiChars = ' .:-+*#%@'
    asciiString = ""

    for y in range(img.height):
        for x in range(img.width):
            brightness = img.getpixel((x, y))
            # takes the min so that no matter what brightness 0-255 always has an index
            index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
            asciiString += asciiChars[index]
        asciiString += "\n"  

    print(asciiString)

def render_ASCII_Greyscale_Image(img):
    asciiChars = " .'`^\",:;I!li><~+_-?[]{}1()|\\//tfrjxnuvczXYUJCQL0OZmwqwpdkbhao*#MW&8%B@$"

    characterFont = ImageFont.load_default()
    bbox = characterFont.getbbox('A')
    charWidth = bbox[2] - bbox[0]
    charHeight = bbox[3] - bbox[1]

    aspectRatioCorrection = 0.55
    canvasWidth = int(img.width * charWidth * aspectRatioCorrection)
    canvasHeight = img.height * charHeight

    canvas = Image.new('L', (canvasWidth, canvasHeight), color="black")
    draw = ImageDraw.Draw(canvas)

    for y in range(img.height):
        for x in range(img.width):
            brightness = img.getpixel((x, y))
            index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
            characterToAdd = asciiChars[index]
            draw.text((x * charWidth * aspectRatioCorrection, y * charHeight), characterToAdd, fill=brightness, font=characterFont)

    canvas.save("./savedImages/ascii_greyscale_image.png")
    canvas.show()

def run():
    imagePath = getImagePath()
    image = getImage(imagePath)
    newWidth = getImageWidth(imagePath)
    resizedImage = resizeImage(image, newWidth)
    create_ASCII_Greyscale(resizedImage)
    render_ASCII_Greyscale_Image(resizedImage)

run()

