import tkinter as tk
import settings
from time import sleep
import whatsapp

class Tooltip:
    def __init__(self, parent, text):
        self.parent = parent
        self.text = text
        self.tooltip_window = None

    def show_tooltip(self, x, y, text, visible):
        if self.tooltip_window:
            self.tooltip_window.destroy()

        self.text = text

        self.tooltip_window = tk.Toplevel(self.parent)
        self.tooltip_window.wm_overrideredirect(True)
        if visible:
            self.tooltip_window.wm_geometry(f"+{x}+{y+20}")
        else:
            self.tooltip_window.wm_geometry(f"+{2000}+{2000}")
        self.tooltip_window.attributes('-topmost', True)  # Keep the tooltip on top of all other windows

        border_color = tk.Frame(self.tooltip_window, background="#404040", highlightbackground="#404040", bd=1)
        label = tk.Label(border_color, text=self.text, background="#232323", relief="solid", borderwidth=0, foreground="#FFFFFF", font=("Courier New", 10))
        label.pack(ipadx=8, ipady=6)
        border_color.pack(ipadx=0, ipady=0)
        
        
tooltipVisible = True
def show_tooltip_at_cursor(tt, root):
    global tooltipVisible
    x, y = root.winfo_pointerxy()
    message = " "
    if tooltipVisible:
        if settings.ReplyMode == True:
            message = settings.SendMessage
        else:
            message = whatsapp.get_last_message()
    tt.show_tooltip(x, y-50, message, tooltipVisible)
    tooltipVisible = not tooltipVisible

if __name__ == "__main__":
    settings.init()
    settings.SendMessage = "Hello world!"
    root = tk.Tk()
    tt = Tooltip(root, "Testing")
    sleep(1)
    show_tooltip_at_cursor(tt, root)
    print("Tooltip should be visible")
    root.mainloop()



