import win32gui
import keyboard
import win32con
from time import sleep

def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

def ListWindows():
    win32gui.EnumWindows(winEnumHandler, None)
            
def set_focus_to_window(window_title):
    # Find the window handle based on the window title
    window_handle = win32gui.FindWindow(None, window_title)

    if window_handle == 0:
        print(f"Window with title '{window_title}' not found.")
        return

    # Set the window to the foreground
    win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(window_handle)

if __name__ == "__main__":
    # Replace 'Your Window Title' with the actual title of the window you want to focus on

    #get the name of the current window
    sleep(2)
    window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    
    set_focus_to_window("WhatsApp - Personal - Microsoft​ Edge")
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    set_focus_to_window(window)


    
    # sleep(0.0001)
    # set_focus_to_window(window)
    

    # Add a delay to observe the focused window (you can remove this in your actual application)
    sleep(3)