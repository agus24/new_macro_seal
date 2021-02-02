import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img
import discord
from constants import *
from datetime import datetime
import auto_purchase
import struct
import os

print(os.path.basename(__file__))
user_id = mouse.getUserId()
print(user_id)
# deret sini jgn di ubah
k = p.keyboard

def process_value(value):
    return struct.pack('@i', value)

while True:
    if keyboard.is_pressed("-"):
        print(mouse.get_freeze_dialog())
        print(mouse.get_item_bank_status())
        print(mouse.getItemValue())
        print(mouse.getPosition())
        sleep(0.2)

    if keyboard.is_pressed("]"):
        value = input("value : ")
        print(value)
        result = mouse.scan_memory(int(value))
        print(result)
        sleep(0.2)
