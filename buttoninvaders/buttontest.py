from gpiozero import Button
from signal import pause

button_1=Button(5)
button_2=Button(6)
button_3=Button(13)

def buttonone ():
    print("Button One")
def buttontwo ():
    print("Button Two")
def buttonthree ():
    print("Button Three")    

while (True):
  
    button_1.when_pressed = buttonone
    button_2.when_pressed = buttontwo
    button_3.when_pressed = buttonthree
    pause ()
