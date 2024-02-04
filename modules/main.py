import ai, frontend, whatsapp, tooltip, keyintercept, settings
import keyboard
import tkinter as tk

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
    whatsapp.init()
    keyintercept.init()

    #Make Frontend
    ui = frontend.GUI()
    
    #Bind hotkeys
    #Enabled toggle
    keyboard.add_hotkey(settings.BIND_TOGGLE_ENABLED, toggle_enabled)
    #Mode Toggle
    keyboard.add_hotkey(settings.BIND_TOGGLE_MODE, toggle_replying)
    #Tooltip Toggle
    tt = tooltip.Tooltip(ui.window, "")
    keyboard.add_hotkey(settings.BIND_TOOLTIP, ui.window.after, args=(0, tooltip.show_tooltip_at_cursor, tt, ui.window))
    #Cancel tooltip with mouse movement

    ui.window.mainloop()
    
def main():
    init()

main()






