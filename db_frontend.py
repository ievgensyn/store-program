from tkinter import *
import db_backend

def get_selected_row(event):
    global selected_row
    index = list1.curselection()[0]
    selected_row = list1.get(index)
    e01.delete(0,END)
    e01.insert(END,selected_row[1])
    e11.delete(0,END)
    e11.insert(END,selected_row[2])
    e21.delete(0,END)
    e21.insert(END,selected_row[3])
    e31.delete(0,END)
    e31.insert(END,selected_row[4])
    e03.delete(0,END)
    e03.insert(END,selected_row[5])
    e13.delete(0,END)
    e13.insert(END,selected_row[6])
    e23.delete(0,END)
    e23.insert(END,selected_row[7])
    e33.delete(0,END)
    e33.insert(END,selected_row[8])
    e43.delete(0,END)
    e43.insert(END,selected_row[9])

def view_command():
    list1.delete(0,END)
    list2.delete(0,END)
    e01.delete(0,END)
    e11.delete(0,END)
    e21.delete(0,END)
    e31.delete(0,END)
    e03.delete(0,END)
    e13.delete(0,END)
    e23.delete(0,END)
    e33.delete(0,END)
    e43.delete(0,END)
    for row in db_backend.view():
        list1.insert(END,row)


warning_message = "You should enter values in fields above!" # if user mistyped in, this message will appear in 'list1'
def insert_command():
    if e01.get()=="" and e11.get()=="" and e21.get()=="" and e31.get()=="" and e03.get()=="" and e13.get()=="" and e23.get()=="" and e33.get()=="" and e43.get()=="":
        list1.delete(0,END)
        list1.insert(END,warning_message)
        pass
    else:
        db_backend.insert(vin_text.get(),auto_text.get(),model_text.get(),year_text.get(),name_text.get(),surmane_text.get(),tel_text.get(),email_text.get(),date_text.get())
        list1.delete(0,END)
        list1.insert(END,(vin_text.get(),auto_text.get(),model_text.get(),year_text.get(),name_text.get(),surmane_text.get(),tel_text.get(),email_text.get(),date_text.get()))
        e01.delete(0,END)
        e11.delete(0,END)
        e21.delete(0,END)
        e31.delete(0,END)
        e03.delete(0,END)
        e13.delete(0,END)
        e23.delete(0,END)
        e33.delete(0,END)
        e43.delete(0,END)

def update_command():
    db_backend.update(selected_row[0],vin_text.get(),auto_text.get(),model_text.get(),year_text.get(),name_text.get(),surmane_text.get(),tel_text.get(),email_text.get(),date_text.get())
    list2.delete(0,END)
    list2.insert(END,"UPDATED!")
    view_command()

info_message = "SELECTED ROW IS DELETED!"
def delete_command():
    db_backend.delete(selected_row[0])
    list2.delete(0,END)
    list2.insert(END,info_message)

def to_uppercase_command(*args):
    vin_text.set(vin_text.get().upper())
#def
window = Tk()
window.title("AVTODELO")

# menubar = Menu(window)
# menubar.add_command(label="Quit",command=window.quit)
# window.config(menu=menubar)

l00 = Label(window,text="VIN")
l00.grid(row=0,column=0,sticky="e")
l10 = Label(window,text="Auto")
l10.grid(row=1,column=0,sticky="e")
l20 = Label(window,text="Model")
l20.grid(row=2,column=0,sticky="e")
l30 = Label(window,text="Year")
l30.grid(row=3,column=0,sticky="e")
l02 = Label(window,text="Name")
l02.grid(row=0,column=2,sticky="e")
l12 = Label(window,text="Surname")
l12.grid(row=1,column=2,sticky="e")
l22 = Label(window,text="Tel.:")
l22.grid(row=2,column=2,sticky="e")
l32 = Label(window,text="EMAIL")
l32.grid(row=3,column=2,sticky="e")
l42 = Label(window,text="Date")
l42.grid(row=4,column=2,sticky="e")
l93 = Label(window,text="-----------------")
l93.grid(row=9,column=3)

vin_text = StringVar()
e01 = Entry(window,textvariable=vin_text,bg='white')
e01.grid(row=0,column=1)
vin_text.trace('w',to_uppercase_command)
auto_text = StringVar()
e11 = Entry(window,textvariable=auto_text,bg='white')
e11.grid(row=1,column=1)
model_text = StringVar()
e21 = Entry(window,textvariable=model_text,bg='white')
e21.grid(row=2,column=1)
year_text = IntVar()
e31 = Entry(window,textvariable=year_text,bg='white')
e31.grid(row=3,column=1)
name_text = StringVar()
e03 = Entry(window,textvariable=name_text,bg='white')
e03.grid(row=0,column=3)
surmane_text = StringVar()
e13 = Entry(window,textvariable=surmane_text,bg='white')
e13.grid(row=1,column=3)
tel_text = StringVar()
e23 = Entry(window,textvariable=tel_text,bg='white')
e23.grid(row=2,column=3)
email_text = StringVar()
e33 = Entry(window,textvariable=email_text,bg='white')
e33.grid(row=3,column=3)
date_text = StringVar()
e43 = Entry(window,textvariable=date_text,bg='white')
e43.grid(row=4,column=3)

list1 = Listbox(window,height=7,width=45,bg='white')
list1.grid(row=5,column=0,rowspan=2,columnspan=2)

list2 = Listbox(window,height=7,width=45,bg='white')
list2.grid(row=7,column=0,rowspan=2,columnspan=2)

# definding and binding list1 with scrollbox (sb1)
sb1 = Scrollbar()
sb1.grid(row=5,column=2,rowspan=2)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)

# definding scrollbar sb2 (just for scrolling rows in list2)
sb2 = Scrollbar()
sb2.grid(row=7,column=2,rowspan=2)
list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

# Button's block
b1 = Button(window,text="View all",width=15,command=view_command)
b1.grid(row=5,column=3)
b2 = Button(window,text="Search",width=15)
b2.grid(row=6,column=3)
b3 = Button(window,text="Add entry",width=15,command=insert_command)
b3.grid(row=7,column=3)
b4 = Button(window,text="Update selected",width=15,command=update_command)
b4.grid(row=8,column=3)
b5 = Button(window,text="Delete selected",width=15,command=delete_command)
b5.grid(row=10,column=3)
b6 = Button(window,text="Quit",command=window.quit)
b6.grid(row=10,column=1,sticky="e")

window.withdraw()
window.update_idletasks()  # Update "requested size" from geometry manager

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position
window.deiconify()
window.mainloop()
