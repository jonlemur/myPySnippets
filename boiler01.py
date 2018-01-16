'''
boiler plate for mini tk app with subthread
By: Jon Aspeheim
'''

import threading
import time
from Tkinter import *

##Use for subthread
def worker():
    while True:
        if someVar:
            print 'Hello'
        time.sleep(2)

# Main function - Startup
def main():
    global someVar
    someVar = True
    myThread = threading.Thread(target=worker)
    myThread.start()

    root = Tk()
    w = Label(root, text="Hello, world!")
    w.pack()
    root.mainloop()

if __name__ == '__main__':
  main()