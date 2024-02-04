import ai, frontend, tooltip, settings
import tkinter as tk
import time

#frontend.MyFloatLayoutApp().run()
def toggle_enabled():
    settings.enabled = not settings.enabled
    print(f"Enabled: {settings.enabled}")

def toggle_replying():
    settings.ReplyMode = not settings.ReplyMode
    if settings.ReplyMode: print("Replying")
    else: print("Reading")

def init():
    #Initialize all modules
    settings.init()

    #Make Frontend
    global ui
    ui = frontend.GUI()
    
    testmsg = "Hello world! This is a test message."
    for char in testmsg:
        settings.KeyQueue.put(char)

    ui.window.mainloop()

def main():
    init()


main()






