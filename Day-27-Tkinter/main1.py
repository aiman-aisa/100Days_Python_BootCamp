from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx=100, pady=100)


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack()

my_label["text"] = "New Text"
# or
my_label.config(text="New Text")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button

def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Entry

input = Entry(width=10)
#input.pack()
print(input.get())
input.grid(column=3, row=3)


new_button = Button(text="New Button", command=button_clicked)
#button.pack()
new_button.grid(column=2, row=0)





window.mainloop()