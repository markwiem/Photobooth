import numpy as np
import cv2, datetime, time

def show_menu(time_elapsed, take_photo, idle):

  if idle:
    menu = cv2.imread('menu.png')
    cv2.imshow('Menu', menu)

  elif time_elapsed <= 1:
    menu = cv2.imread('menu1.png')
    cv2.imshow('Menu', menu)

  elif time_elapsed <= 2:
   menu = cv2.imread('menu2.png')
   cv2.imshow('Menu', menu)

  elif time_elapsed <= 3:
    menu = cv2.imread('menu3.png')
    cv2.imshow('Menu', menu)

  elif time_elapsed <= 3.95:
    menu = cv2.imread('menu4.png')
    cv2.imshow('Menu', menu)