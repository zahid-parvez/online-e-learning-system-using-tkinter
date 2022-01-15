from tkinter import *

from new_user import new_user
from old_user import old_user


def user():
    def driver_for_old_user_window():
        user_login_window.destroy()
        old_user()

    def driver_for_new_user_window():
        user_login_window.destroy()
        new_user()

    user_login_window = Tk()
    user_login_window.geometry("800x600")
    Label(user_login_window, text="User's LOG IN / SIGN UP", bg='grey', fg='indigo', font=("Wide Latin", 27)).pack()
    user_login_window.title("User's LOG IN / SIGN UP")
    login_label = Label(user_login_window, text="Already have an account : ", font=('Arial Rounded MT Bold', 12))
    login_label.place(x=200, y=100)
    signup_label = Label(user_login_window, text="New to our learning site  :",
                         font=('Arial Rounded MT Bold', 12))
    signup_label.place(x=200, y=150)
    login_button = Button(user_login_window, text="     **Login**     ", bg="Blue", activeforeground="Blue",
                          font=('Arial Rounded MT Bold', 12), command=driver_for_old_user_window)
    login_button.place(x=450, y=100)
    signup_button = Button(user_login_window, text="Sign up for free", bg="Green", activeforeground="green",
                           font=('Arial Rounded MT Bold', 12), command=driver_for_new_user_window)
    signup_button.place(x=450, y=150)
    exit_button_for_user = Button(user_login_window, text="      EXIT       ", bg="red", activeforeground="green",
                                  font=('Arial Rounded MT Bold', 12), command=user_login_window.destroy)
    exit_button_for_user.place(x=170, y=190)
    user_login_window.mainloop()
