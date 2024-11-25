from cv2 import cvtColor, COLOR_BGR2GRAY
from skimage.feature import corner_moravec, corner_harris
from util import getCurrTimeMs, printCompletedStarting, MatLike, bcolors


# https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.corner_harris
def detectCornersHarris(image: MatLike, blockSize = 2, ksize = 3, k = 0.04) -> MatLike:
    print(f"{bcolors.HEADER}Detecting corners using Harris...{bcolors.ENDC}")
    startMs = getCurrTimeMs()

    gray = cvtColor(image, COLOR_BGR2GRAY)
    result = corner_harris(gray)
    src = image.copy()
    src[result>0.01*result.max()]=[0, 255, 0]
    printCompletedStarting(startMs)

    return src


# https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.corner_moravec
def detectCornersMoravec(image: MatLike) -> MatLike:
    print(f"{bcolors.HEADER}Detecting corners using Moravec...{bcolors.ENDC}")
    startMs = getCurrTimeMs()

    gray = cvtColor(image, COLOR_BGR2GRAY)
    result = corner_moravec(image=gray, window_size=1)
    src = image.copy()
    src[result>0.01*result.max()]=[0, 0, 255]
    printCompletedStarting(startMs)

    return src