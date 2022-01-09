try:
    # Python2
    import Tkinter as tk #Tkinter or tkinter is for keyboard input
except ImportError:
    # Python3
    import tkinter as tk


def action(event):
    # userInput to set as global scope since it will be used in another function outside of this function
    global userInput
    if event.keysym == 'Escape':
        userInput = "Escape"
    else:
        userInput = event.keysym
    # destroy() => to kill the loop after a key is pressed. This will terminate this whole module and cannot reuse
    # quit() => will just stop the mainloop() and can reuse!!
    keyPress.quit()


def keyboard_input():
    # mainloop() => the main loop to check keyboard input
    keyPress.mainloop()
    return userInput

def destroy():
    # terminates the mainloop completely
    keyPress.destroy()
    activate()
    keyPress.mainloop()

# the main object or function to utilize this keyboard
def activate():
    global keyPress
    keyPress = tk.Tk()
    # useful method to specify what each key stroke does
    keyPress.bind_all('<Key>', action)
    # withdraw() => don't show the tk window
    keyPress.withdraw()  


activate()



