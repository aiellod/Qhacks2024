import ai, frontend, whatsapp, tooltip, keyintercept, settings
import keyboard
import tkinter as tk

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
    #whatsapp.init()
    keyintercept.init()

    #Make Frontend
    ui = tk.Tk()
    
    #Bind hotkeys
    #Enabled toggle
    keyboard.add_hotkey(settings.BIND_TOGGLE_ENABLED, toggle_enabled)
    #Mode Toggle
    keyboard.add_hotkey(settings.BIND_TOGGLE_MODE, toggle_replying)
    #Tooltip Toggle
    keyboard.add_hotkey(settings.BIND_TOOLTIP, tooltip.make_and_show_tooltip, args=(ui,))

    testmsg = "Hello world! This is a test message."
    for char in testmsg:
        settings.KeyQueue.put(char)

    ui.mainloop()
    


def main():
    init()

main()






