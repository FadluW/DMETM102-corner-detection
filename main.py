import cv2

from util import bcolors, saveImageWithName
from corner_detection import detectCornersHarris, detectCornersMoravec

# Modify file name accordingly
originalFileName = "original.png"
originalImage = cv2.imread(filename=originalFileName, flags=cv2.IMREAD_GRAYSCALE)

if originalImage is None:
    raise Exception("Image not loaded, please check path.")

print(f"{bcolors.OKGREEN}Image {originalFileName} loaded.{bcolors.ENDC}")
print(f"{bcolors.BOLD}Dimensions:{bcolors.ENDC} {originalImage.shape[1]}x{originalImage.shape[0]}")
print(f"{bcolors.BOLD}Colors:{bcolors.ENDC} GRAYSCALE\n")

saveImageWithName(detectCornersMoravec(originalImage), "corner-detection-moravec")
saveImageWithName(detectCornersHarris(originalImage), "corner-detection-harris")

print(f"{bcolors.OKGREEN}\nAll done!\n{bcolors.ENDC}")