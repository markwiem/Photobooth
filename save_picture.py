import numpy as np
import cv2, datetime

picname = "foo"

def save(frame, location):
    global picname
    name = str(datetime.datetime.now())
    # strip the trailing seconds decimals
    name, foo, bar = name.rpartition('.')
    name = name.replace(":", ".", 2)
    name = name.replace(" ", "_")

    #rename all '/' to '_' so shutil does not mistake
    #  'hour/min/sec' in filename for filepath
    #  note that OSX seems to retype or rename all
    #  ':' that are written by datetime.datetime.now()
    #  to '/' in the filesystem
    name = name.replace("/", "_")
    filename = name + "_Wiemer-Flewelling_Wedding.png"
    picname = filename
    cv2.imwrite(location + filename, frame)

def get_name():
    return picname
