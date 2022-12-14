import time

from pygame import mixer
from datetime import datetime
from time import sleep
from tkinter import *
from threading import Thread #allows multiple functions to work at the same time

#cr1 = "#feffff"  # White

window = Tk()
window.title("")
window.geometry('350x150')
#window.configure(background=cr1)
window.resizable(width=False, height=False)

def ring_alarm():
    #mixer.init()  # Initializing the mixer
    mixer.music.load('sound1.mp3')
    mixer.music.play()

def alarm():
    while True:
        control = 1
        c_hour = "07"
        c_minutes = "13"
        c_seconds = "00"
        c_period = "PM".upper()

        current_time = datetime.now()

        hour = current_time.strftime("%I")
        minut = current_time.strftime("%M")
        second = current_time.strftime("%S")
        period = current_time.strftime("%p")

        if control==1:
            if c_period == period:
                if c_hour == hour:
                    if c_minutes == minut:
                        if c_seconds == second:
                            print("Time to take a break")
                            ring_alarm()
        sleep(1)

# Creating the thread
# Allows multiple functions to work at the same time

t1 = Thread(target=alarm)

t1.start()
mixer.init()

window.mainloop()