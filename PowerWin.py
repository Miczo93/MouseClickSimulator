from pynput.mouse import Button, Controller, Listener
import time as t
import sys 
from datetime import datetime, date
global olddate

def next(s,points):
  if mouse.position != (1250,575):
    sys.exit("Koniec")
  mouse.press(Button.left)
  t.sleep(0.1)
  mouse.release(Button.left)
  t.sleep(s - 0.1)
  print(points)

def letsplay():
    mouse.position = (1250,575)
    mouse.click(Button.left, 1)
    t.sleep(0.5)
    next(1.83,300)
    next(1,550)
    next(1,850)
    next(0.4,1000)
    next(0.3,1200)
    next(0.4,1450)
    next(0.6,1550)
    next(1,1750)
    next(1,1950)
    next(0.75,2000)
    next(1.1,2500)
    next(1,2650)
    next(1.1,2750)
    next(0.9,2950)
    next(1.2,3250)
    next(1.25,3400)
    next(0.9,3700)
    next(1.2,4150)
    next(1,4300)
    next(0.9,4450)
    next(0.9,4750)



    next(200,0)#last jump

def on_click(x, y, button, pressed):
    if pressed:
        teraz = datetime.now().time()
        global olddate
        print(datetime.combine(date.today(), teraz) - datetime.combine(date.today(), olddate))
        olddate = teraz

def testuj():
    global olddate
    olddate = datetime.now().time()
    with Listener(on_click=on_click) as listener:
        listener.join()

        
mouse = Controller()
#testuj()
letsplay()

#https://poweryourday.win.eu.panasonic.com/pl/game
