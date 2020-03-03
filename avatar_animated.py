from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

s = SenseHat()

def main():
  
  l = (0, 0, 0)
  M = (50, 50, 250)
  
  R = [230, 40, 43] #red
  B = [55, 112, 182] #blue
  G = [50, 133, 29] #green
  P = [255,105,180] #pink
  Y = [244, 230, 0] #yellow
  O = [255,140,0] #orange
  W = [242, 242, 242] #white
  H = [166, 81, 57] #brown
  E = [0, 0, 0] #black
  S = [247, 198, 167] #skincolor

  avatar1 = [
  E,E,R,R,R,W,E,E,
  E,E,R,R,R,R,R,E,
  E,H,S,H,E,S,E,E,
  E,H,S,S,H,H,S,E,
  E,E,H,S,S,S,E,E,
  E,R,R,Y,B,B,Y,E,
  W,E,B,B,B,B,R,W,
  E,E,H,E,E,E,H,E
  ]


  avatar2 = [
    E,E,G,G,G,W,E,E,
    E,E,G,G,G,G,G,E,
    E,H,S,H,E,S,E,E,
    E,H,S,S,H,H,S,E,
    E,E,H,S,S,S,E,E,
    E,G,G,Y,B,B,Y,E,
    W,E,B,B,B,B,G,W,
    E,E,H,E,E,E,H,E
  ]

  avatar3 = [
    E,E,P,P,P,W,E,E,
    E,E,P,P,P,P,P,E,
    E,H,S,H,E,S,E,E,
    E,H,S,S,H,H,S,E,
    E,E,H,S,S,S,E,E,
    E,P,P,Y,B,B,Y,E,
    W,E,B,B,B,B,P,W,
    E,E,H,E,E,E,H,E
    ]

  avatar4 = [
    E,E,O,O,O,W,E,E,
    E,E,O,O,O,O,O,E,
    E,H,S,H,E,S,E,E,
    E,H,S,S,H,H,S,E,
    E,E,H,S,S,S,E,E,
    E,O,O,Y,B,B,Y,E,
    W,E,B,B,B,B,O,W,
    E,E,H,E,E,E,H,E
    ]

  array = [avatar1, avatar2, avatar3, avatar4]
  
  while True : 
  	for x in array :
  		digit = randint(0,3)
  		s.set_pixels(array[digit])
  		sleep(1)
  		s.clear()
          
try:
    main()
    
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
    
finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)