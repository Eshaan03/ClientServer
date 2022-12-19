from tkinter import *
import sqlite3
import os as op
root = Tk()
myLabel = Label(root, text="Hello World")
'''
conn = sqlite3.connect('table3.db')
c = conn.cursor()
c.execute("""CREATE TABLE table_info(
                                      regno text,
                                      name text,
                                      dept text
                                     )""")
conn.commit()
conn.close()
'''
def submit():
    conn = sqlite3.connect('table3.db')
    c = conn.cursor()
    c.execute("INSERT INTO table_info VALUES (:regno, :name, :dept)",
                 {
                     'regno': regno.get(),
                     'name': name.get(),
                     'dept': dept.get()
                     #'age': age.get(),
                     #'gender':gender.get()
                     #'gender1': gender1.get(),
                     #'gender2': gender2.get()
                 } )
    regno.delete(0,END)
    name.delete(0,END)
    dept.delete(0,END)
    #age.delete(0,END)
    conn.commit()
    conn.close()
# Creating Labels
v = StringVar(root, value="CSE")
regno = Entry(root, width=30, textvariable=v)
regno.grid(row=0, column=1)
name = Entry(root, width=30)
name.grid(row=1, column=1)
dept = Entry(root, width=30,)
dept.grid(row=2, column=1)
gender1 = Radiobutton(root, text="Male", value=1)
gender1.grid(row=3, column=0)
gender2 = Radiobutton(root, text="Female", value=2)
gender2.grid(row=3, column=1)
age = Spinbox(root, from_=0, to=100)
age.grid(row=4, column=1)
# Creating Text box labels

regno = Label(root, text="RegNo")
regno.grid(row=0, column=0)
name = Label(root, text="Name")
name.grid(row=1, column=0)
dept = Label(root, text="Dept")
dept.grid(row=2, column=0)
#gender = Label(root, text="Gender")
#gender.grid(row=3, column=0)
#age = Label(root, text="Age")
#age.grid(row=4, column=0)

insert_button = Button(root, text="Insert", command=submit)
insert_button.grid(row=5, column=0, columnspan=1, pady=20, padx=1, ipadx=10)

update_button = Button(root, text="Update", command=submit)
update_button.grid(row=5, column=1, columnspan=2, pady=10, padx=10, ipadx=10)

delete_button = Button(root, text="Delete", command=submit)
delete_button.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=10)

select = Button(root, text="Select", command=submit)
select.grid(row=6, column=1, columnspan=2, pady=10, padx=20, ipadx=10)
root.mainloop()
