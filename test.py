import os
import psutil
import pymem
import time
import keyboard
from window import setup_ui


def getProcess() :
    processes = pymem.process.list_processes()
    for value in processes:
        if value.szExeFile == b'SO3D.exe':
            return value
        pass
    return False


def getItemValue():
    calc = (pointerStat) + 1056 + (116)
    pymem.memory.read_short(pc, calc)

inputData = None
print(os.path.basename(__file__))

while True :
    pm = pymem.Pymem()
    if getProcess() :
        process = getProcess()
        pid = process.th32ProcessID
        pc = pymem.process.open(pid)
        baseAddressMouse = int(0x400000) + int(0x00DD5F24)
        baseAddressStat = int(0x400000) + int(0x003DA400)        
        try:
            pointerStat = pymem.memory.read_int(pc, baseAddressStat)
            getItemValue()
            print(pid)
        except:
            print("error")
        else:
            print(
                "1. cegel\n",
                "2. ant nest\n",
                "3. inden\n",
                "4. ant crus\n",
                "5. auto tempa\n",
                "6. farm srs\n",
                "0. ts\n"
            )
            inputData = input("Answer ? ") or "0"
    else:
        print('process not found')
    if inputData == "1":
        print("opening cegel.py")
        import cegelcmd      
    elif inputData == "2":
        print("opening ant.py")
        import ant
    elif inputData == "3":
        print("opening inden.py")
        import inden
    elif inputData == "4":
        print("opening ant.py")
        import ant_crus
    elif inputData == "5":
        print("opening auto_tempa.py")
        import auto_tempa
    elif inputData == "6":
        print("opening srs_hunt.py")
        import srs_hunt
    elif inputData == "0":
        print("opening ts.py")
        import ts
    time.sleep(0.5)
