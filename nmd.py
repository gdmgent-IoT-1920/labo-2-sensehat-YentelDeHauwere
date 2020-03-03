from sense_hat import SenseHat
from random import randint
import time

s = SenseHat()

s.set_rotation(270)

string = input("Geef een woord in:")
array = list(string)

speed = input("Geef de snelheid in seconden:")

def main():
  
  while True:
      for x in array:
        s.show_letter(x, [randint(0,255), randint(0,255), randint(0,255)])
        time.sleep(float(speed))
        s.clear()
      time.sleep(3)
      
try:
  main()
  
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")

finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)