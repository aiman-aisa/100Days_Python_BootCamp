from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=50)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# label
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_calculated = Label(text="0")
label_calculated.grid(column=1, row=1)

label_km = Label(text="KM")
label_km.grid(column=2, row=1)

def calculate():
    miles = float(input.get())
    km = round(miles * 1.60934)
    label_calculated.config(text=f"{km}")


calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()