from config import *

if MOCKED:
    from hardware import mocked as lib
else:
    from hardware import real as lib

led_lib = lib.LedLib()
button_lib = lib.ButtonLib()
