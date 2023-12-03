from PIL import Image
import time

filename = "buildings.jpg"
with Image.open(filename) as img:
     img.load()


tailleimage = img.size

print("The size of picture is " + str(tailleimage))

time.sleep(3600)
