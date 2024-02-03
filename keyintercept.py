import keyboard
from time import sleep

messagepos = 0
message = "I love big slimy yummy tasty feet, please let me eat them all day long"

def key_press(event):
    global messagepos
    if event.event_type == keyboard.KEY_DOWN and len(event.name) == 1 and messagepos < len(message):
        sleep(0.000001)
        keyboard.press_and_release('backspace')
        keyboard.write(message[messagepos])
        messagepos += 1

keyboard.hook(key_press)

keyboard.wait()