from tkinter import *
from tkinterflow import *       # ! Very important, put this right after import of tkinter functions


def t_flow():
    root = Tk()
    my_frame = Frame(root)                 # Very Important!, you cannot use .flow() methods in root
    my_frame.pack(fill=BOTH, expand=True)  # Very Important!, frame must stick to parent container walls

    button1 = Button(my_frame, text="----Button1---")
    button1.flow()

    button2 = Button(my_frame, text="Button2")
    button2.flow()

    button3 = Button(my_frame, text="----Button3---")
    button3.flow()

    button4 = Button(my_frame, text="Button4")
    button4.flow()

    root.mainloop()


def t_pack():
    root = Tk()
    my_frame = Frame(root)  # Very Important!, you cannot use .flow() methods in root
    my_frame.pack(fill=BOTH, expand=True)  # Very Important!, frame must stick to parent container walls

    button1 = Button(my_frame, text="----Button1---")
    button1.pack()

    button2 = Button(my_frame, text="Button2")
    button2.pack()

    button3 = Button(my_frame, text="----Button3---")
    button3.pack()

    button4 = Button(my_frame, text="Button4")
    button4.pack()

    root.mainloop()


def t_flow2():

    root = Tk()

    buttons=[]

    myframe=Frame(root)

    myframe.pack(fill=BOTH, expand=True)

    button1=Button(myframe, text="---Place---",command = lambda: organizeWidgetsWithPlace(myframe))
    button1.pack()

    button2=Button(myframe, text="Grid",command = lambda: organizeWidgetsWithGrid(myframe))
    button2.pack()

    button3=Button(myframe, text="Stop Organizing", command = lambda: stopOrganizingWidgets(myframe))

    for i in range(10):
        buttons.append(Button(myframe, text="button"+str(i)))

    root.mainloop()


if __name__ == "__main__":
    # t_pack()
    # t_flow()
    t_flow2()

