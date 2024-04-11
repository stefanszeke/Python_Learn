import tkinter

# window
window = tkinter.Tk()
window.title("Cool App")
window.minsize(width=200, height=300)
window.config(padx=50, pady=80)


def testFunction():
    try:  
        miles = float(my_entry.get())
        km = convertMilesToKm(miles)
        my_label3.config(text=km)
    except:
        my_label3.config(text="Invalid input")
        
def convertMilesToKm(miles):
    return miles * 1.60934

# entry miles
my_entry = tkinter.Entry(
    width=15,
)
my_entry.grid(row=0, column=1)
my_entry.focus()

# label miles
my_label1 = tkinter.Label(text="Miles")
my_label1.grid(row=0, column=2)

# labels rows 1
my_label2 = tkinter.Label(text="Miles")
my_label2.grid(row=1, column=0)

my_label3 = tkinter.Label(text="0")
my_label3.grid(row=1, column=1)

my_label4 = tkinter.Label(text="Km")
my_label4.grid(row=1, column=2)

# button
my_button = tkinter.Button(
    text="Convert",
    font=("Arial", 10, "bold"),
    command=testFunction
)
my_button.grid(row=2, column=1)



window.mainloop()
