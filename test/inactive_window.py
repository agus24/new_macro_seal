from time import sleep
from subprocess import Popen
import pywinauto
import keyboard


while True:
    try:
        app = pywinauto.Application(backend="uia").connect(class_name="SO3D")
    except KeyboardInterrupt:
        break
    except Exception as error:
        print(error)
        sleep(0.2)
    else:
        print("Ready")
        while True:
            if keyboard.is_pressed("-"):
                dialog = app.Dialog.child_window(class_name_re='^Seal Online.*$')
                dialog = app.Dialog.window
                print(dialog)
                print(dir(dialog))
                # dialog.controls.send_chars("agus244")
                # app.controls.send_chars("agus244")
                print(app.window)
                print(dir(app.window))
