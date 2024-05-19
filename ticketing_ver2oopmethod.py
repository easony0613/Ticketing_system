'''
Purpose: to create a ticketing system for parents to buy tickets for their children
date: 13/05/24
version 1: being able to see the GUI
version 2: The GUI will calculate the price of the tickets and show it on the total price label. 
Version 2 part 2: I have not used any OOP method in the previous version 2, so in this version 2 I will use the OOP method
'''

from tkinter import *
from tkinter import ttk

ADULT = 15
CHILD = 5
STUDENT = 10

class Ticket():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_sub_total(self):
        total = self.price * self.quantity
        return total

def collect_ticket():
    '''Create an object for each ticket type and store them in a list'''
    order_list = []
    order_list.clear()
    order_list.append(Ticket(ADULT,int(adult_amount.get())))
    order_list.append(Ticket(CHILD,int(child_amount.get())))
    order_list.append(Ticket(STUDENT,int(student_amount.get())))
    return order_list

def calculate_price():
    total_price = 0
    for order in (collect_ticket()):
        total_price += order.calculate_sub_total()
    total_detail.set(f"Total: ${total_price}")
        


root = Tk()
root.title("Ticketing system")
root.geometry("600x200")
child_amount = IntVar()
adult_amount = IntVar()
student_amount = IntVar()
total_detail = StringVar()

adult_amount.set("0")
child_amount.set("0")
student_amount.set("0")
total_detail.set("Total: $0")
total_price = 0 # i added total price

root.resizable(0,0)

label1 = ttk.Label(root, text="Adult   $15", font=("Arial 20 bold"))
label1.grid(row=0, column=0, padx=10, sticky="W")

label2 = ttk.Label(root, text="Child   $5", font=("Arial 20 bold"))
label2.grid(row=1, column=0, padx=10, sticky="W")

label3 = ttk.Label(root, text="Student/senior   $10", font=("Arial 20 bold"))
label3.grid(row=2, column=0, columnspan=2, padx=10, sticky="W")

label4 = ttk.Label(root, textvariable=total_detail, font=("Arial 20 bold")) # i changed the total price label from text to a text variable so it can be easily updated using a function
label4.grid(row=3, column=0, padx=10, sticky="W")

entry1 = Entry(root, textvariable=adult_amount)
entry1.grid(row=0, column=2)

entry2= Entry(root, textvariable=child_amount)
entry2.grid(row=1, column=2)

entry3 = Entry(root, textvariable=student_amount)
entry3.grid(row=2, column=2)

button1 = Button(root, text="Calculate", font=("Arial 20 bold"), command=calculate_price)
button1.grid(row=3, column=2, padx=10, pady=3)



root.mainloop()
