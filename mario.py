from sense_hat import SenseHat
from time import sleep
import sys

s = SenseHat()

R = [230, 40, 43] #red
B = [55, 112, 182] #blue
Y = [244, 230, 0] #yellow
W = [242, 242, 242] #white
H = [166, 81, 57] #brown
E = [0, 0, 0] #black
S = [247, 198, 167] #skincolor
LB = [1, 1, 1] #light blue

mario = [
LB,LB,R,R,R,W,LB,LB,
LB,LB,R,R,R,R,R,LB,
LB,H,S,H,E,S,LB,LB,
LB,H,S,S,H,H,S,LB,
LB,LB,H,S,S,S,LB,LB,
LB,R,R,Y,B,B,Y,LB,
W,LB,B,B,B,B,R,W,
LB,LB,H,LB,LB,LB,H,LB
    ]

mario_jump = [
LB,LB,R,R,R,R,R,LB,
LB,H,S,H,E,S,LB,LB,
LB,H,S,S,H,H,S,LB,
W,LB,H,S,S,S,LB,LB,
LB,R,R,Y,B,B,Y,W,
LB,LB,B,B,B,B,R,LB,
LB,H,LB,LB,LB,H,LB,LB,
LB,LB,LB,LB,LB,LB,LB,LB,
    ]

def main():
    while True:
        s.set_pixels(mario)
        event = s.stick.wait_for_event()
        if(event.direction == 'up' and event.action == 'pressed'):
           s.set_pixels(mario_jump)
           sleep(1)
           s.set_pixels(mario)
      
try:
  main()
  
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")

finally:
    print("Opkuisen van de matrix")
    s.clear()
    sys.exit(0)
