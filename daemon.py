import pyperclip
from database import *

while True:
    clipboard_data = pyperclip.paste()
    records = get_records()
    if records:
        if clipboard_data != records[-1]['data']:
            add_record(clipboard_data)
            print(f"Записал \"{clipboard_data}\"")
    else:
        add_record(clipboard_data)
        print(f"Записал \"{clipboard_data}\"")
