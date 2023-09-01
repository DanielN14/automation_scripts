import os
import random
import ctypes

SPI_SETDESKWALLPAPER = 20
wallPapersDir = "C:\\Users\\..."

dirContent = os.listdir(wallPapersDir)
images = []

for file in dirContent:
    if os.path.isfile(os.path.join(wallPapersDir, file)) and file.endswith('.jpg'):
        images.append(file)

wallPaperToSet = os.path.join(wallPapersDir, images[random.randint(0, len(images))-1]);


ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallPaperToSet, 3)