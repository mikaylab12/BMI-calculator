# Mikayla Beelders
from tkinter import *
from tkinter import messagebox

#  Get height value from entry
def get_height():
    height = float(entry_h.get())
    return round(height)

# Get weight from entry
def get_weight():
    weight = float(entry_w.get())
    return round(weight)

def calculate_bmi(b=""):   # Because the bind function gives an argument to the function, I have put b there
    print(b)
# In order to calculate the result
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = round(weight / (height ** 2))
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter a positive height:")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid inputs:")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)

if __name__ == '__main__':
    root = Tk()
    root.title("Body Mass Index Calculator")
    root.bind("<Return>", calculate_bmi)
    root.geometry("700x700")
    root.configure(bg="#9900ff")
    root.resizable(width=False, height=False)

    frame = Frame(root, width=590, height=430, relief='raised', bg='#b84dff')
    frame.place(relx=0.08, rely=0.1)
    # heading label
    label_heading = Label(root, bg="#b84dff",fg ="white", text="IDEAL BODY MASS INDEX CALCULATOR", font=("Helvetica", 15, "bold"), pady=5)
    label_heading.place(relx=0.2, rely=0)

    # weight entry and label
    label_w = Label(root, bg="#b84dff",fg ="white", text="Enter Weight (in kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    label_w.place(x=155, y=160)
    entry_w = Entry(root, bg="#9900ff",fg ="white", bd=8, width=6, font="Helvetica")
    entry_w.place(x=370, y=160)

    # height entry and label
    label_h = Label(root, bg="#b84dff",fg ="white", text="Enter Height (in cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    label_h.place(x=155, y=121)
    entry_h = Entry(root,bg="#9900ff",fg ="white",  bd=8, width=6, font="Helvetica")
    entry_h.place(x=370, y=121)

    # BMI button
    BUTTON = Button(bg="#9900ff", fg ="white",bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.place(x=250, y=350)

gender =Label(frame, text="Gender:", bg='#b84dff',fg ="white")
gender.place(relx=0.18, rely=0.35)

age = Label(frame, text="Age:", bg='#b84dff', fg='white')
age.place(relx=0.18, rely=0.45)
age_entry = Entry(frame, bg="#9900ff", state='readonly')
age_entry.place(relx=0.35, rely=0.45)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal', bg="#b84dff")
    else:
        age_entry.config(state='readonly')

gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.35, rely=0.35)

root.mainloop()