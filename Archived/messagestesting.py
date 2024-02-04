import ctypes
import ctypes.wintypes
import win32con
import win32gui
import win32process
import win32security
import sys
from time import sleep
import win32api

def is_admin():
    """
    Check if the current user has administrative privileges.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_message_text(hwnd):
    """
    Get the text of a window.
    """
    length = win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
    buffer = ctypes.create_unicode_buffer(length + 1)
    win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, length + 1, buffer)
    return buffer.value

def send_message(hwnd, message):
    """
    Send a message to a window.
    """
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, message)
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def enum_windows_callback(hwnd, lParam):
    """
    Callback function for enumerating windows.
    """
    process_id = ctypes.wintypes.DWORD()
    try:
        thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
    
        # Skip windows that are not accessible
        try:
            process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, process_id)
            win32security.OpenProcessToken(process_handle, win32security.TOKEN_QUERY)
        except:
            return True
        
        # Check if the process is the current Python script
        if process_id == win32process.GetCurrentProcessId():
            return True

        # Get the window text and print it
        window_text = get_message_text(hwnd)
        print(f"Received message: {window_text}")

        # Respond to the message
        # response = "This is a response."
        # send_message(hwnd, response)

    except Exception as error:
        print(f"Error: {error}")
        return input("Press Enter to continue...")

    return input("Press Enter to continue...")
    return True

def main():
    """
    Main function that enumerates windows and responds to messages.
    """
    if is_admin():
        win32gui.EnumWindows(enum_windows_callback, 0)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    main()
