from sense_hat import SenseHat
from random import randint
from time import sleep
import sys

s = SenseHat()

def main():

  speed = input("Geef de snelheid in seconden:")
  
  matrix1 = 0
  matrix2 = 0

  while True:
      
      s.set_pixel(matrix1, matrix2, [randint(1,255), randint(1,255), randint(1,255)])
      sleep(float(speed))
      s.clear()
      
      if matrix2 == 7 and matrix1 == 7:
          matrix1 = 0
          matrix2 = 0
          
      elif matrix2 == 7:
          matrix2 = 0
          matrix1 += 1
          
      else:
          matrix2 +=1
        
try:
    main()
    
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
    
finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)