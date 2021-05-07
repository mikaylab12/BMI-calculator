# Mikayla Beelders
from tkinter import *
# defining the functions
# calculating the BMI
def calc_BMI():
    calc_BMI = (int(entry_w.get()))/(int(entry_h.get()/100)**2)
    label_bmi.set(calc_BMI)
# calculating the Ideal BMI
def calc_IdealBMI():
    weight_value= entry_w.get()
    height_value= entry_h.get()
    calc_IdealBMI = (0.5*(int(weight_value))/(int(height_value/100)**2)+11.5)
    label_ibmi.set(calc_IdealBMI)
# clearing the numbers
def clear_numbers():
    entry_w.delete(0, END)
    entry_h.delete(0, END)
    entry_a.delete(0, END)
# exiting the program
def exit_program():
    return root.destroy()

root=Tk()
# var=IntVar
label_text=StringVar
root.geometry ("600x600")
root.title("Ideal Body Mass Index")
Text="Ideal Body Mass Index Calculator"
frame_1 = Frame(root, width=10, height=2, highlightbackground = 'black', highlightthickness = 2)
frame_1.pack(fill="both", expand="yes")
heading = Label(frame_1, text="Ideal Body Mass Index Calculator")
heading.pack()
text = Label(frame_1, text="Enter your weight, height and gender")
text.pack()
# weight label and entry as well as their places
label_w= Label(frame_1, text= "Weight: ")
label_w.place(x=20, y=80)
entry_w= Entry(frame_1)
entry_w.place(x=80, y=80)
label_kg = Label(frame_1, text="Kilograms")
label_kg.place(x=250, y=80)

# height label and entry as well as their places
label_h= Label(frame_1, text= "Height: ")
label_h.place(x=20, y=120)
entry_h= Entry(frame_1)
entry_h.place(x=80, y=120)
label_cm = Label(frame_1, text="cm")
label_cm.place(x=250, y=120)
# age label and entry as well as their places
label_a= Label(frame_1, text= "Age: ")
label_a.place(x=360, y=120)
entry_a= Entry(frame_1)
entry_a.place(x=400, y=120)
# gender label and selector
label_g= Label(frame_1, text= "Gender: ")
label_g.place(x=20, y=160)
genders = [
    "Select",
    "Male",
    "Female",
]
clicked= StringVar()
clicked.set(genders[0])

drop = OptionMenu(root, clicked, *genders)
drop.pack(pady=20)
drop.place(x = 80, y=160)
#BMI label_
label_bmi= Label(root, text= "BMI: ")
label_bmi.place(x=20, y=350)
entry_bmi= Entry(root)
entry_bmi.place(x=80, y=350)
#IBMI label
label_ibmi= Label(root, text= "Ideal BMI: ")
label_ibmi.place(x=330, y=350)
entry_ibmi= Entry(root)
entry_ibmi.place(x=400, y=350)
# The necessary buttons
# Calculating BMI
calc_button = Button (root, text="Calculate your Ideal Body Mass Index", command=calc_BMI)
calc_button.place(x=150, y=200)
# Clear numbers
clear_button = Button (root, text="Clear", command=clear_numbers)
clear_button.place(x=20, y=540)
# Exit program
exit_button = Button (root, text="Exit", command=exit_program)
exit_button.place(x=520, y=540)

root.mainloop()