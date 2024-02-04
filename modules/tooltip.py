import tkinter as tk

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
        

def on_timer():
    x, y = root.winfo_pointerxy()
    tooltip.show_tooltip(x, y-50)

if __name__ == "__main__":
    root = tk.Tk()
    tooltip = Tooltip(root, "This is a tooltip!")

    # Set the main window initially invisible
    root.attributes("-alpha", 0.0)

    # Schedule the timer to trigger after 3 seconds
    root.after(3000, on_timer)

    root.mainloop()
