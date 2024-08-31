import os.path
from PIL import Image

# First I need to get an input images from the user
# Also need to validate if that image path actually exists

imagePathValid = False

while (imagePathValid == False):
    imagePath = input("Enter the image path to convert to ASCII...\n")
    if (os.path.isfile(imagePath) == True):
        imagePathValid = True
        print("Valid image path.")
    else:
        print("Error: Image not found")

# I need to convert the image into grayscale

img = Image.open(imagePath).convert('L')
img.save("greyscale.png")
