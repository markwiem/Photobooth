import os

def do_it(make_happen, location, filename):

  if make_happen:
          try:
            os.system("lpr -o media=Custom.4x6.25in " + location + "/" + filename)
          except:
              pass
  else:
      pass
