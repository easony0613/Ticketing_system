'''
Purpose: to create a ticketing system for parents to buy tickets for their children
date: 13/05/24
version 1: being able to see the GUI
'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ticketing system")
root.geometry("600x200")
adult_amount = DoubleVar()
adult_amount.set("")
child_amount = DoubleVar()
child_amount.set("")
student_amount = DoubleVar()
student_amount.set("")

label1 = ttk.Label(root, text="Adult   $15", font=("Arial 20 bold"))
label1.grid(row=0, column=0, padx=10, sticky="W")

label2 = ttk.Label(root, text="Child   $5", font=("Arial 20 bold"))
label2.grid(row=1, column=0, padx=10, sticky="W")

label3 = ttk.Label(root, text="Student/senior   $10", font=("Arial 20 bold"))
label3.grid(row=2, column=0, columnspan=2, padx=10, sticky="W")

label4 = ttk.Label(root, text="Total price: ", font=("Arial 20 bold"))
label4.grid(row=3, column=0, padx=10, sticky="W")

entry1 = Entry(root, textvariable=adult_amount)
entry1.grid(row=0, column=2)

entry2= Entry(root, textvariable=child_amount)
entry2.grid(row=1, column=2)

entry3 = Entry(root, textvariable=student_amount)
entry3.grid(row=2, column=2)

button1 = Button(root, text="Calculate", font=("Arial 20 bold"))
button1.grid(row=3, column=2, padx=10, pady=3)

root.mainloop()