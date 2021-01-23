import psutil
import pymem
import time
import keyboard

def getProcess() :
    processes = pymem.process.list_processes()
    for value in processes:
        if value.szExeFile == b'SO3D.exe':
            return value
        pass
    return False

def getItemValue() :
    slot = []
    item = []
    for i in range(0, 40) :
        calc = (pointerStat) + 1056 + (116*i)
        # print(calc)
        slot.append(calc)
        item.append(pymem.memory.read_short(pc, calc))
    return item

while True :
    pm = pymem.Pymem()
    if getProcess() :
        process = getProcess()
        pid = process.th32ProcessID
        pc = pymem.process.open(pid)
        baseAddressMouse = int(0x400000) + int(0x00DD5F24)
        baseAddressStat = int(0x400000) + int(0x003DA400)        
        pointerStat = pymem.memory.read_int(pc, baseAddressStat)
        try :
            getItemValue()
            print(pid)
        except :
            print("error")
        else :
            print(
                "1. inden jibit\n"
            )
    else :
        print('process not found')
    if keyboard.is_pressed("1") :
        print("opening indenjibit.py")
        import indenjibit
    time.sleep(0.5)
        