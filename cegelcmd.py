import keyboard
from time import sleep
import pyautogui
import pywinauto as p
import win32api
import macro
import imgread as img
import checkProcess


class Macro():

    def __init__(self):
        import mouseSeal as mouse

        self.mouse = mouse
        self.k = p.keyboard
        self.m = p.mouse

        print(
            "PID : "+ str(self.mouse.getPid()) + "\n"
        )

        start = True
        # i = imagesearch
        while start:
            if keyboard.is_pressed('-') :
                print("Starting Hunt..")
                runHunt()
            if keyboard.is_pressed(']') :
                self.mouse.getPosition()
                # mouse.getItemQty()
                sleep(0.3)

            if keyboard.is_pressed('=') :
                print('Script Stopped.')
                start = False
                break

            if checkProcess.check_pid() :
                start = False
                break

    def sellItem(self) :
        print('Selling Item..')
        self.mouse.moveMouse(555, 227)
        sleep(0.5)
        self.macro.mouseClick()
        sleep(0.5)
        while img.checkImage("./img/shop.jpg") == False :
            self.k.send_keys('{ENTER}')
            sleep(0.5)
            self.mouse.moveMouse(394, 296)
            self.macro.mouseClick()
            sleep(0.5)
        sleep(0.5)
        self.macro.sellSlot1()
        self.macro.sellSlot2()
        self.macro.sellSlot3()
        self.macro.sellSlot4()
        self.macro.sellSlot5()
        sleep(1)
        print("escape")

    def runHunt(self) :
        print("Hunt Started..")
        # pos = i.imagesearch("./img/shop.JPG")
        start_hunt = True
        while start_hunt :
            if img.checkImage("./img/shop.jpg") :
                sleep(0.5)
                self.k.send_keys("{VK_ESCAPE}")
            self.mouse.moveMouse(379, 335)
            macro.mouseClick()
            if keyboard.is_pressed('c') :
                print('Hunt Stopped.')
                start_hunt = False
                break
            inventory = self.mouse.getItemValue()
            print(inventory)
            for i in range(0,5) :
                if inventory[i] == 300 :
                    print('Item Full Detected.')
                    sellItem()
                    print("Hunt Continue..")
            self.k.send_keys(
                "{q down}"
                "{q up}"
            )
            sleep(0.5)
            self.k.send_keys(
                "{F5}"
            )
            sleep(2)
            for x in range(0,10) :
                self.k.send_keys("{SPACE}")
                sleep(0.05)
                self.k.send_keys("{SPACE}")
                sleep(0.05)
                self.k.send_keys("{SPACE}")
                sleep(0.05)
                self.k.send_keys("{SPACE}")
                sleep(0.05)
                if keyboard.is_pressed('c') :
                    print('Hunt Stopped.')
                    start_hunt = False
                    break
