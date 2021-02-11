from tkinter import *


def m_to_km():
    """This function converts the meter input to kilometer"""
    meter = float(m_input.get())
    kilometer = meter / 1000
    km_input.delete('0', 'end')
    km_input.insert(END, string=kilometer)


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
km_input.insert(END, '0')
km_input.grid(column=2, row=0)

# km_result = Label(text=" ", font=("Arial", 24, "bold"))
# km_result.grid(column=2, row=0)

km_label = Label(text="Kilometer", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=m_to_km)
calc_button.grid(column=1, row=3)
calc_button.config(padx=5, pady=5)

# Keep the interface open until exited
interface.mainloop()
