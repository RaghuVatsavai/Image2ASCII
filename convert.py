import os.path
from PIL import Image

imagePathValid = False
while not imagePathValid:
    imagePath = input("Enter the image path to convert to ASCII...\n")
    if os.path.isfile(imagePath):
        imagePathValid = True
        print("Valid image path.")
    else:
        print("Error: Image not found")

img = Image.open(imagePath).convert('L')
img.save("greyscale.png")

newWidth = 100
width, height = img.size
aspectRatio = height / width
newHeight = int(newWidth * aspectRatio * 0.55)
img = img.resize((newWidth, newHeight))

asciiChars = '.:-+*#%@'

asciiString = ""

for i in range(img.height):
    for j in range(img.width):
        brightness = img.getpixel((j, i))
        index = min(brightness // (256 // len(asciiChars)), len(asciiChars) - 1)
        asciiString += asciiChars[index]
    asciiString += "\n"  

print(asciiString)

