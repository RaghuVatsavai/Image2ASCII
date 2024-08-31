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

# What ASCII characters will I use?
# I could use ".:-+*#%@"
# The denser characters should correlate to the more intense pixels like #%@
# The lighter characters should correlate to the lower intense pixels like .:-+

# Test to loop through all the pixels and print their brightness

brightnessValues = []

for i in range(img.width):
    for j in range(img.height):
        brightness = img.getpixel((i, j))
        brightnessValues.append(brightness)

print(len(brightnessValues))
print("Max Val:", max(brightnessValues))