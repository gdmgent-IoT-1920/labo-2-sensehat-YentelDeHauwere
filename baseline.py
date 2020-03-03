from sense_hat import SenseHat
from random import randint
import sys

s = SenseHat()

s.set_rotation(270)

def main():
  while True:
    s.show_message('Hello! We are New Media Development :)', 
                  text_colour=[randint(0, 255), randint(0, 255), randint(0, 255)], 
                  back_colour=[randint(0, 255)*0.1, randint(0, 255)*0.1, randint(0, 255)*0.1])
              
try:
  main()
  
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")

finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)