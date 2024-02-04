import keyboard
from time import sleep
import queue
import settings
import whatsapp

def key_press(event):
    # If a key is pressed and the message queue is not empty )
    if event.event_type == keyboard.KEY_DOWN and settings.enabled and settings.KeyQueue.qsize() > 0:
        key = event.name
        if key == 'enter':
            sleep(0.000001)
            keyboard.press_and_release('ctrl+backspace')
            keyboard.press_and_release('backspace')
            whatsapp.send_message(settings.SendMessage)
            settings.SendMessage = ""
        elif (len(key) == 1 or key == 'space') and not key in ['*', '(', ')']: #letters symbols and numbers, not shortcuts
            sleep(0.000001)
            keyboard.press_and_release('backspace')
            keyboard.write(settings.KeyQueue.get())
            if key == 'space':
                settings.SendMessage += ' '
            else:
                settings.SendMessage += key
        

def init():
    keyboard.hook(key_press)


testmessage = "Hello world! This is a test message."
if __name__ == "__main__":

    for char in testmessage:
        settings.KeyQueue.put(char)

    init()
    keyboard.wait()
    