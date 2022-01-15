from tkinter import *
from tkinter import messagebox

import welcomewindow
from add_course import add_course
from courses import admin_display_courses
from fun_back_from_add_course import fun_back_from_add_course, fun_back_from_remove_course
from remove_course import remove_course
from view_students_details import view_student_details


def administrative_window(admin_name):
    admin_personal_window = Tk()

    def driver_function_admin_course():
        admin_personal_window.destroy()
        admin_display_courses()

    def driver_function_add_course():
        admin_personal_window.destroy()
        add_course()
        fun_back_from_add_course(admin_name)

    def driver_function_remove_course():
        admin_personal_window.destroy()
        remove_course()
        fun_back_from_remove_course(admin_name)

    def driver_function_student_details():
        # admin_personal_window.destroy()
        view_student_details()

    def driver_function_log_out():
        messagebox.showinfo('Successfully Logged out', "Changes Are Updated If Any")
        admin_personal_window.destroy()
        welcomewindow.welcomewindow()

    admin_personal_window.title(f" Welcome {admin_name} ")
    lbl = Label(admin_personal_window, text="   Admin Window   ", fg='indigo', font=("Wide Latin", 27), bg="grey")
    lbl.pack()
    btn1 = Button(admin_personal_window, text=" Add Courses ", bg="Green", fg='white', activeforeground="Blue",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_add_course)
    btn1.place(x=250, y=120)
    btn2 = Button(admin_personal_window, text="  Remove Course  ", bg="Blue", fg='white', activeforeground="green",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_remove_course)
    btn2.place(x=250, y=190)
    btn3 = Button(admin_personal_window, text="Display Courses ", bg="Violet", fg='white', activeforeground="Indigo",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_admin_course)
    btn3.place(x=250, y=260)
    btn3 = Button(admin_personal_window, text="View Student Details", bg="yellow", fg='white',
                  activeforeground="Indigo",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_student_details)
    btn3.place(x=250, y=330)
    btn4 = Button(admin_personal_window, text="          Log Out            ", bg="red", fg="black",
                  activeforeground="red", font=('Arial Rounded MT Bold', 12), width=20, height=2,
                  command=driver_function_log_out)
    btn4.place(x=250, y=400)
    admin_personal_window.geometry("700x500")
    admin_personal_window.mainloop()
