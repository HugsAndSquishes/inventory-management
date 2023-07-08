from tkinter import *
#from tkinter import ttk
from tkinter.messagebox import showinfo
class MainWindow():
    def __init__(self):
        root = Tk()
        root.title('Inventory Management')
        root.geometry('500x150')
        self.root = root
        self.windows = {}
        self.current_window = ''

        nav_bar = Frame(root)
        nav_bar.grid(row=0, column=0, sticky=(W, E))

        #self.nav_buttons = {}
        self.nav_bar = nav_bar

    def add_nav_button(self, target_window_name, order):
        button = Button(self.nav_bar, text=target_window_name, command=lambda: self.open_window(target_window_name)).grid(column=order, row=0, sticky=(N, S))
        #self.nav_buttons[target_window_name] = button

    def add_window(self, name, frame):
        frame.grid(row=1, column=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        self.windows[name] = frame

    def open_window(self, name):
        print(self.windows)
        target_window = self.windows.get(name)
        print(f"REQUEST TO OPEN {name}")
        print(target_window)
        if target_window:
            target_window.tkraise()
            print(f'{name} OPENED') 

    def close_window(self):
        # TODO: is this needed?
        if self.current_window:
            pass

    def switch_window(self, target_window):
        # TODO: is this needed?
        self.close_window(self.current_window)



class Inventory():
    def __init__(self,product):
        self.product=product

    def add_product(self,product):
        myfile=open("Data.txt",'r+')
        data=myfile.readlines()
        if product in data:
            return 0
        else:
            return 1
        
#labels for home screen
def homescreen(main):
    root = main.root
    frame=Frame(root, width=500, height=250)
    frame.place(x=0,y=0)
    welcome=Label(frame, text='Please choose from the following options')
    welcome.grid(row=0, column=3)

    newproduct=Button(frame, text='Add new product to file', command=lambda: main.open_window("Add product"))
    newproduct.grid(row=1, column=1)

    removeproduct = Button(frame, text='Remove product from file', command=lambda: main.open_window("Remove product"))
    removeproduct.grid(row=3, column=1)

    addinventory = Button(frame, text='Add inventory for existing product to file', command=homescreen)
    addinventory.grid(row=1, column=3)

    removeinventory = Button(frame, text='Remove inventory for existing product from file',command=homescreen)
    removeinventory.grid(row=3, column=3)

    updatebalance=Button(frame, text='Update balance for existing product', command=homescreen)
    updatebalance.grid(row=5, column=1)

    return frame

def screen1(main):
    root = main.root
    frame1=Frame(root, width=500, height=250)
    message=Label(frame1, text='Please enter name of product you want to add the file')
    message.grid(row=0, column= 3)
    productnamebox=Entry(frame1)
    productnamebox.grid(row=1,column=2)
    productname=Label(frame1, text='Name of product:')
    productname.grid(row=1,column=1)
    productquantity=Label(frame1, text='Quantity:')
    productquantity.grid(row=2,column=1)
    quanbox=Entry(frame1)
    quanbox.grid(row=2,column=2)
    return frame1

def screen2(main):
    root = main.root
    frame2=Frame(root, width=500, height=250)
    message=Label(frame2, text='Please enter name of product you want to remove from file')
    message.grid(row=0, column= 3)
    productnamebox=Entry(frame2)
    productnamebox.grid(row=1,column=2)
    productname=Label(frame2, text='Name of product:')
    productname.grid(row=1,column=1)
    productquantity=Label(frame2, text='Quantity:')
    productquantity.grid(row=2,column=1)
    quanbox=Entry(frame2)
    quanbox.grid(row=2,column=2)
    return frame2

def screen3(main):
    root = main.root
    frame2=Frame(root, width=500, height=250)
    message=Label(frame2, text='Please enter name of product you want add inventory')
    message.grid(row=0, column= 3)
    productnamebox=Entry(frame2)
    productnamebox.grid(row=1,column=2)
    productname=Label(frame2, text='Name of product:')
    productname.grid(row=1,column=1)
    productquantity=Label(frame2, text='Quantity:')
    productquantity.grid(row=2,column=1)
    quanbox=Entry(frame2)
    quanbox.grid(row=2,column=2)
    return frame2

main_window = MainWindow()

main_window.add_window("Add product", screen1(main_window))
main_window.add_window("Remove product", screen2(main_window))

main_window.add_window("Homescreen", homescreen(main_window))
main_window.add_nav_button("Homescreen", 0)

main_window.open_window("Homescreen")

main_window.root.mainloop()