import tkinter as tk
import settings
from time import sleep

class Tooltip:
    def __init__(self, parent, text):
        self.parent = parent
        self.text = text
        self.tooltip_window = None

    def show_tooltip(self, x, y):
        if self.tooltip_window:
            self.tooltip_window.destroy()

        self.tooltip_window = tk.Toplevel(self.parent)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y+20}")

        label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=2, ipady=2)

def make_and_show_tooltip(root):
    if settings.ReplyMode == True:
        message = "Replying"
    else:
        message = "Reading"

    tooltip = Tooltip(root, message)
    x, y = root.winfo_pointerxy()
    tooltip.show_tooltip(x, y-50)
    print("Tooltip should be visible")


if __name__ == "__main__":
    settings.init()
    root = tk.Tk()
    root.attributes("-alpha", 0.0)
    sleep(2)
    make_and_show_tooltip(root)
    print("Tooltip should be visible")
    root.mainloop()



