BIND_TOGGLE_ENABLED = 'ctrl+shift+8'
BIND_TOGGLE_MODE = 'ctrl+shift+9'
BIND_TOOLTIP = 'ctrl+shift+0'

import queue


#Shared globals
def init():
    global enabled
    global ReplyMode #True in typing mode, false in read mode
    global KeyQueue
    global SendMessage
    enabled = True
    ReplyMode = True
    KeyQueue = queue.Queue()
    SendMessage = ""
