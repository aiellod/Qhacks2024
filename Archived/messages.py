import win32gui
import keyboard
import win32con
import win32api
import win32process
import pyuac
from time import sleep



def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

def ListWindows():
    win32gui.EnumWindows(winEnumHandler, None)

if __name__ == "__main__":
    WinOriginal = win32gui.GetForegroundWindow()

    window_handle = win32gui.FindWindow(None, "WhatsApp - Personal - Microsoft​ Edge")
    win32gui.SetForegroundWindow(window_handle)
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    win32gui.SetForegroundWindow(WinOriginal)
    

    # Add a delay to observe the focused window
    print("Done")
    sleep(3)

    