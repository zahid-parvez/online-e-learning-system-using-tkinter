from tkinter import *
from tkinter import messagebox

# import welcomewindow
# from display_user_courses import display_user_courses
# from display_courses import display_courses
from display_user_courses import display_user_courses
from registerToCourse import registerToCourse
from take_exam import take_exam
from videoCourses import videoCourses


def logged_in_user(user_name):
    def driver_function_my_course():
        user_pers_window.destroy()
        videoCourses()
        logged_in_user(user_name)

    def driver_function_register_course():
        user_pers_window.destroy()
        registerToCourse()
        logged_in_user(user_name)

    def driver_function_write_exam():
        user_pers_window.destroy()
        take_exam(user_name)
        logged_in_user(user_name)

    def driver_display_courses_rand():
        display_user_courses()
        pass

    def driver_function_log_out():
        messagebox.showinfo('Successfully Logged out', "            Thank You            ")
        user_pers_window.destroy()
        # import welcomewindow


    user_pers_window = Tk()
    user_pers_window.title(f" Welcome back {user_name} ")
    Label(user_pers_window, text=f" Welcome back {user_name}", fg='indigo', font=("Wide Latin", 27), bg="grey").pack()
    btn1 = Button(user_pers_window, text="Video Lectures", bg="Green", fg='white', activeforeground="Blue",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_my_course)
    btn1.place(x=250, y=120)
    btn2 = Button(user_pers_window, text="Register into new course", bg="Blue", fg='white', activeforeground="green"
                  , height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_register_course)
    btn2.place(x=250, y=190)
    btn3 = Button(user_pers_window, text=" Write Exam ", bg="Violet", fg='white', activeforeground="Indigo",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_function_write_exam)
    btn3.place(x=250, y=260)
    btn3 = Button(user_pers_window, text=" My Courses ", bg="yellow", fg='white',
                  activeforeground="Indigo",
                  height=2, font=('Arial Rounded MT Bold', 12), width=20, command=driver_display_courses_rand)
    btn3.place(x=250, y=330)
    btn4 = Button(user_pers_window, text="          Log Out            ", bg="red", fg="black",
                  activeforeground="red", font=('Arial Rounded MT Bold', 12), width=20, height=2,
                  command=driver_function_log_out)
    btn4.place(x=250, y=400)
    user_pers_window.geometry("700x500")
    user_pers_window.mainloop()

# logged_in_user("Zahid")
