import matplotlib.pyplot as plt
import math
import numpy as np
import time
import os
import cv2

# Types for type-hinting
from cv2.typing import MatLike

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getCurrTimeMs() -> int:
    return int(time.time() * 1000)


def printCompletedStarting(startMs: int) -> None:
    print(f"Completed in: {bcolors.BOLD}{int(time.time() * 1000) - startMs}{bcolors.ENDC}ms\n")


def saveImageWithName(image: MatLike, name: str) -> None:
    targetDirectory = "./results/"

    if not os.path.exists(targetDirectory):
        os.mkdir(targetDirectory)

    path = f"{targetDirectory}{name}.png"
    cv2.imwrite(path, image)

    print(f"{bcolors.OKGREEN}Saved image in {path}{bcolors.ENDC}\n")
