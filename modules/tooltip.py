import tkinter as tk
import settings
from time import sleep

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

        label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=2, ipady=2)
        
        
tooltipVisible = True
def show_tooltip_at_cursor(tt, root):
    global tooltipVisible
    x, y = root.winfo_pointerxy()
    if settings.ReplyMode == True:
        message = "Replying"
    else:
        message = "Reading"
    print(tooltipVisible)
    tt.show_tooltip(x, y-50, message, tooltipVisible)
    tooltipVisible = not tooltipVisible

if __name__ == "__main__":
    settings.init()
    root = tk.Tk()
    root.attributes("-alpha", 0.0)
    sleep(2)
    show_tooltip_at_cursor(root)
    print("Tooltip should be visible")
    sleep(2)
    root.mainloop()



