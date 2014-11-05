import numpy as np
import cv2, save_picture

picture = 0

def blenderize(images):
    global picture
    #establish padding, positions, & scale for pics
    padX1 = 120
    padY1 = 30

    padX2 = 120
    padY2 = 425

    padX3 = 120
    padY3 = 825

    scaleY = .7
    scaleX = .7

    # Load three images, remember file path!
    img1 = cv2.imread('/Users/markwiem/Documents/CODE/PROJECTS/Photobooth/Photos/' + images[0])
    img2 = cv2.imread('/Users/markwiem/Documents/CODE/PROJECTS/Photobooth/Photos/' + images[1])
    img3 = cv2.imread('/Users/markwiem/Documents/CODE/PROJECTS/Photobooth/Photos/' + images[2])
    background = cv2.imread('Background.png')

    #Resize relevant images to fit on target paper
    img1 = cv2.resize(img1, None, fx=scaleX, fy=scaleY, interpolation = cv2.INTER_AREA)
    img2 = cv2.resize(img2, None, fx=scaleX, fy=scaleY, interpolation = cv2.INTER_AREA)
    img3 = cv2.resize(img3, None, fx=scaleX, fy=scaleY, interpolation = cv2.INTER_AREA)

    #Establish image size in rows, columns
    y1, x1, chan1 = img1.shape
    y2, x2, chan2 = img2.shape
    y3, x3, chan3 = img3.shape
    y4, x4, chan4 = background.shape

    #Make and Merge ROIs to background
    roi_1 = img1[0:y1, 0:x1]
    background[padY1:y1+padY1, padX1:x1+padX1] = roi_1

    roi_2 = img2[0:y2, 0:x2]
    background[padY2:y2+padY2, padX2:x2+padX2] = roi_2

    roi_3 = img3[0:y3, 0:x3]
    background[padY3:y3+padY3, padX3:x3+padX3] = roi_3

    #Rescale background for eval purposes
    #background = cv2.resize(background, None, fx=.5, fy=.5, interpolation = cv2.INTER_AREA)
    picture = background

def get_file():
    return picture
