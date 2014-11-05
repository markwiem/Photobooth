import numpy as np
import cv2, datetime, time, save_picture, photo_print, blender, serial
from menu import show_menu

pics_to_take = 3
do_print = True
#save individual pics here:
save_pics_to = '/Users/markwiem/Documents/CODE/PROJECTS/Photobooth/Photos/'
#save finalized pic here:
save_final_to = '/Users/markwiem/Documents/CODE/PROJECTS/Photobooth/Photos/Photobooth_Photos/'
scale_x = .5
scale_y = .5
img_list = []

ser = serial.Serial('/dev/tty.usbserial-DC008MPQ', 9600, timeout=0)

cap = cv2.VideoCapture(1)

#quick = cv2.imread('quick.png')

while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  trigger = ser.readline(100)

  # Display the resulting frame
  frame = cv2.resize(frame, None, fx= scale_x, fy= scale_y, interpolation = cv2.INTER_AREA)
  cv2.imshow('Lindsey & Mark are Married!', frame)

  #turn the UI led on while photo-session is not in progress
  ser.write(str(1))

  show_menu(0, False, True)

  if "Button" in trigger:
      start_time = time.time()
      numPics = 0
      #turn the UI led off while photo-session is in progress
      ser.write(str(0))

      #take the requested num pics in photobooth style
      while (numPics < pics_to_take):
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx= scale_x, fy= scale_y, interpolation = cv2.INTER_AREA)
        cv2.imshow('Lindsey & Mark are Married!', frame)
        elapsed_time = time.time() - start_time

        show_menu(elapsed_time, False, False)

        if elapsed_time >= 4:
          #show_menu(0, True, False)
          time.sleep(1.5)
          #save each photo taken
          save_picture.save(frame, save_pics_to)
          img_list.append(save_picture.get_name())
          numPics += 1
          start_time = time.time()
        else:
          pass

      #use the blender function to create the finished picture
      #load blender function with pic names in python list
      blender.blenderize(img_list)

      #save & print final photobooth pic
      save_picture.save(blender.get_file(), save_final_to)
      photo_print.do_it(do_print, save_final_to, save_picture.get_name())

      #reset variables
      img_list = []
      numPics = 0

  else:
    pass


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
