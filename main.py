from tkinter import *

# Instance of Tk
interface = Tk()

# Default settings
interface.title("Meter to Kilometer Converter")
interface.minsize(width=400, height=300)
interface.config(padx=100, pady=100)

# The interface settings
m_input = Entry(width=10)
m_input.grid(column=0, row=0)

m_label = Label(text="Meter", font=("Arial", 18, "normal"))
m_label.grid(column=0, row=1)

equal_label = Label(text="=", font=("Arial", 24, "bold"))
equal_label.grid(column=1, row=0)

km_input = Entry(width=10)
km_input.grid(column=2, row=0)

km_label = Label(text="Kilometer", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate")
calc_button.grid(column=1, row=3)

# Keep the interface open until exited
interface.mainloop()

