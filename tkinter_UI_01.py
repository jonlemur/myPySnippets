from Tkinter import *

root = Tk()
root.title('Hello tKinter')
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(460, 350))

def fBTN1():
    print "click1"

def fBTN2():
    print "click2"
    lbl1Text.set('Hi Jon')



top_frame = Frame(root, bg='dark slate grey', width = 460, height=50, pady=3).grid(row=0, columnspan=5)
mid_frame = Frame(root, bg='dim grey', width = 460, height=300, pady=3).grid(row=1, columnspan=3)

btn1 = Button(top_frame, text="Button #1",bd=0, bg='slate grey',  command=fBTN1).grid(row = 0, columnspan = 1)
btn2 = Button(top_frame, text="Button #2",bd=0, bg='slate grey', command=fBTN2).grid(row = 0, columnspan = 3)

## If u want to change a lable dynamicly make it usa a var as text
lbl1Text = StringVar()
lbl1Text.set('Hello World')
label1 = Label(mid_frame, textvariable=lbl1Text, bd=0, bg='dim grey').grid(row = 1, columnspan = 3)


root.mainloop()
