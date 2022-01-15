from tkinter import *
from tkinter import messagebox

from admin import admin
from display_courses import display_courses
from user import user


def welcomewindow():
    def driver_display_courses():
        welcome_window.destroy()
        display_courses()

    def driver_admin():
        welcome_window.destroy()
        admin()

    def exitMsg():
        messagebox.showinfo('Thank You', "Thank You For Using Our Application ")
        welcome_window.destroy()

    welcome_window = Tk()
    lbl = Label(welcome_window, text="   Welcome Window   ", fg='indigo', font=("Wide Latin", 27), bg="grey")
    lbl.place(x=30, y=50)
    btn1 = Button(welcome_window, text="         USER            ", bg="Green", activeforeground="Blue", height=2,
                  font=('Arial Rounded MT Bold', 12), width=20, command=user)
    btn1.place(x=250, y=120)
    btn2 = Button(welcome_window, text="        ADMIN        ", bg="Blue", activeforeground="green", height=2,
                  font=('Arial Rounded MT Bold', 12), width=20, command=driver_admin)
    btn2.place(x=250, y=190)
    btn3 = Button(welcome_window, text="Display Courses ", bg="Yellow", activeforeground="Indigo", height=2,
                  font=('Arial Rounded MT Bold', 12), width=20, command=driver_display_courses)
    btn3.place(x=250, y=260)
    btn4 = Button(welcome_window, text="          Exit            ", bg="red", fg="black",
                  font=('Arial Rounded MT Bold', 12), width=20, height=2, command=exitMsg)
    btn4.place(x=250, y=330)

    welcome_window.title('Online E-education GUI')
    welcome_window.geometry("700x500")
    welcome_window.mainloop()
