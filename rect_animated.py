from sense_hat import SenseHat
from time import sleep
import sys

s = SenseHat()

def main():
  
  l = (0, 0, 0)
  M = (50, 50, 250)

  small = [
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, l, M, M, l, l, l,
  	l, l, l, M, M, l, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  ]

  medium = [
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, M, M, M, M, l, l,
  	l, l, M, l, l, M, l, l,
  	l, l, M, l, l, M, l, l,
  	l, l, M, M, M, M, l, l,
  	l, l, l, l, l, l, l, l,
  	l, l, l, l, l, l, l, l,
  ]

  large = [
  	l, l, l, l, l, l, l, l,
  	l, M, M, M, M, M, M, l,
  	l, M, l, l, l, l, M, l,
  	l, M, l, l, l, l, M, l,
  	l, M, l, l, l, l, M, l,
  	l, M, l, l, l, l, M, l,
  	l, M, M, M, M, M, M, l,
  	l, l, l, l, l, l, l, l,
  ]

  extralarge = [
  	M, M, M, M, M, M, M, M,
  	M, l, l, l, l, l, l, M,
  	M, l, l, l, l, l, l, M,
  	M, l, l, l, l, l, l, M,
  	M, l, l, l, l, l, l, M,
  	M, l, l, l, l, l, l, M,
  	M, l, l, l, l, l, l, M,
  	M, M, M, M, M, M, M, M,
  ]

  while True:
      s.set_pixels(small)
      sleep(1)
      s.set_pixels(medium)
      sleep(1)
      s.set_pixels(large)
      sleep(1)
      s.set_pixels(extralarge)
      sleep(1)
      s.set_pixels(large)
      sleep(1)
      s.set_pixels(medium)
      sleep(1)
      s.set_pixels(small)
      sleep(1)
      
          
        
try:
    main()
    
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
    
finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)