import keyboard
from time import sleep

def key_press(event):
    if event.event_type == keyboard.KEY_DOWN and len(event.name) == 1:
        print(event.name)
        keyboard.press_and_release('backspace')
        keyboard.write('a')

keyboard.hook(key_press)

keyboard.wait()
