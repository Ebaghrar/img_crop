from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
     img.load()


tailleimage = img.size

print("The size of picture is " + str(tailleimage))

