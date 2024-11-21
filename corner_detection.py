from skimage.feature import corner_moravec, corner_harris
from util import getCurrTimeMs, printCompletedStarting, MatLike, bcolors


# https://docs.opencv.org/4.10.0/dc/d0d/tutorial_py_features_harris.html
def detectCornersHarris(image: MatLike, blockSize = 2, ksize = 3, k = 0.04) -> MatLike:
    print(f"{bcolors.HEADER}Detecting corners using Harris...{bcolors.ENDC}")
    startMs = getCurrTimeMs()

    result = corner_harris(image)
    # src[result>0.01*result.max()]=[0,0,255]
    printCompletedStarting(startMs)

    return result


# https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.corner_moravec
def detectCornersMoravec(image: MatLike) -> MatLike:
    print(f"{bcolors.HEADER}Detecting corners using Moravec...{bcolors.ENDC}")
    startMs = getCurrTimeMs()

    result = corner_moravec(image=image)
    printCompletedStarting(startMs)
    
    return result