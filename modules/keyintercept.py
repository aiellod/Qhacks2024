import keyboard
from time import sleep
import queue
import settings

def key_press(event):
    # If a key is pressed and the message queue is not empty )
    a = event.event_type == keyboard.KEY_DOWN and len(event.name) == 1 
    b = settings.enabled == True and settings.KeyQueue.qsize() > 0
    if a and b:
        sleep(0.000001)
        keyboard.press_and_release('backspace')
        if not event.name in ['*', '(', ')']:
            keyboard.write(settings.KeyQueue.get())

def init():
    keyboard.hook(key_press)


testmessage = "Hello world! This is a test message."
if __name__ == "__main__":

    for char in testmessage:
        settings.KeyQueue.put(char)

    init()
    keyboard.wait()
    