import cv2

from util import bcolors

# Modify file name accordingly
originalFileName = "original.jpg"
originalImage = cv2.imread(filename=originalFileName)

if originalImage is None:
    raise Exception("Image not loaded, please check path.")

print(f"{bcolors.OKGREEN}Image {originalFileName} loaded.{bcolors.ENDC}")
print(f"{bcolors.BOLD}Dimensions:{bcolors.ENDC} {originalImage.shape[1]}x{originalImage.shape[0]}")
print(f"{bcolors.BOLD}Colors:{bcolors.ENDC} {originalImage.shape[2]}\n")

print(f"{bcolors.OKGREEN}\nAll done!\n{bcolors.ENDC}")