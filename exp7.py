'''exp no 7 
GUI program using tkinter '''
'''
Exp 7: Write a python program to implement GUI Application using Tkinter

Theory
    Tkinter is the standard GUI library for Python. 
    Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
    Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

    Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called widgets.
    There are currently 15 types of widgets in Tkinter. We present these widgets as well as a brief description in the following table 
    1	Button
    The Button widget is used to display buttons in your application.

    2	Canvas
        The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.

    3	Checkbutton
        The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.

    4	Entry
        The Entry widget is used to display a single-line text field for accepting values from a user.

    5	Frame
        The Frame widget is used as a container widget to organize other widgets.

    6	Label
        The Label widget is used to provide a single-line caption for other widgets. It can also contain images.

    7	Listbox
        The Listbox widget is used to provide a list of options to a user.

    8	Menubutton
        The Menubutton widget is used to display menus in your application.

    9	Menu
        The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.

    10	Message
        The Message widget is used to display multiline text fields for accepting values from a user.

    11	Radiobutton
        The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.

    12	Scale
        The Scale widget is used to provide a slider widget.

    13	Scrollbar
        The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.

    14	Text
        The Text widget is used to display text in multiple lines.

    15	Toplevel
        The Toplevel widget is used to provide a separate window container.

    16	Spinbox
        The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.

    17	PanedWindow
        A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.

    18	LabelFrame
        A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.

    19	tkMessageBox
        This module is used to display message boxes in your applications.



@author: KHAN SHOAB AKHTAR VAKIL AHMAD (19CO33)

'''


class App:
    def __init__from tkinter import *

(self):
        self.root=Tk()
        self.root.title('GUI App')
        self.root.geometry('500x350')
        self.root.configure(background='light blue')
        #Labels are created
        self.rollno = Label(self.root, text="Roll No.", bg="light blue")
        self.name = Label(self.root, text="Name", bg="light blue")
        self.address = Label(self.root, text="Address", bg="light blue")
        self.mob = Label(self.root, text="Mobile", bg="light blue")
        #Labels are added on window
        self.rollno.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.address.grid(row=2,column=0)
        self.mob.grid(row=3,column=0)
        #Textfields are created
        self.rollnof = Entry(self.root)
        self.namef = Entry(self.root)
        self.addressf = Entry(self.root)
        self.mobf = Entry(self.root)
        #Textfields are added on window
        self.rollnof.grid(row=0,column=1,ipadx='100')
        self.namef.grid(row=1,column=1,ipadx='100')
        self.addressf.grid(row=2,column=1,ipadx='100')
        self.mobf.grid(row=3,column=1,ipadx='100')
        #Submit button created and added on window
        self.submit = Button(self.root, text="Submit", fg="Black", bg="light green", command=self.insert) 
        self.submit.grid(row=8, column=1,sticky=W+E)
        #Clear button created and added on window
        self.clear = Button(self.root, text="Clear",fg="Black", bg="light green", command=self.clearAll) 
        self.clear.grid(row=8, column=0,sticky=W+E)  
        self.root.mainloop()
    def insert(self):
        with open('student.csv','a') as file:
            rec=self.rollnof.get()+','+self.namef.get()+','+self.addressf.get()+','+self.mobf.get()+'\n'
            #rec=self.rollnof.get()+';'
            file.write(rec)

        
    def clearAll(self):
        self.rollnof.delete(0,'end')
        self.namef.delete(0,'end')
        self.addressf.delete(0,'end')
        self.mobf.delete(0,'end')

def main():
    myapp = App()

if __name__=='__main__':
    main()




'''
Conclusion

    1] Created a GUI App using tkinter
    2] Learnt different wedges of tkinter

'''
