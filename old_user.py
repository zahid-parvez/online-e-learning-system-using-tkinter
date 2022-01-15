from tkinter import *
from tkinter import messagebox
from logged_in_user import logged_in_user


def user_personal_window(user_name):
    logged_in_user(user_name)


def old_user():
    def verify_user():
        user_id = user_id_entry.get()
        user_password = user_password_entry.get()
        if user_password != 'vasavi@1':
            messagebox.showwarning(title="please try again", message="Incorrect password/user_id")
        else:
            old_user_login_window.destroy()
            user_personal_window(user_id)

    old_user_login_window = Tk()
    old_user_login_window.title("** USER's LOGIN **")
    old_user_login_window.geometry("700x500")
    lbl = Label(old_user_login_window, text="   ** USER's LOGIN **   ", fg='indigo', font=("Wide Latin", 27), bg="grey")
    lbl.place(x=30, y=50)
    user_id_label = Label(old_user_login_window, text="Enter your user-id : ", font=('Arial Rounded MT Bold', 12))
    user_id_label.place(x=200, y=160)
    user_password_label = Label(old_user_login_window, text="Enter your password  :",
                                font=('Arial Rounded MT Bold', 12))
    user_password_label.place(x=200, y=200)
    user_id_entry = Entry(old_user_login_window, width=20, borderwidth=5)
    user_id_entry.place(x=450, y=160)
    user_password_entry = Entry(old_user_login_window, width=20, borderwidth=5)
    user_password_entry.place(x=450, y=200)
    verify_user_button = Button(old_user_login_window, text="Verify and Login", bg="Blue", activeforeground="Green",
                                font=('Arial Rounded MT Bold', 12), command=verify_user)
    verify_user_button.place(x=130, y=300)
    exit_button = Button(old_user_login_window, text="       EXIT       ", bg="red",
                         font=('Arial Rounded MT Bold', 12), command=old_user_login_window.destroy)
    exit_button.place(x=500, y=300)
    old_user_login_window.mainloop()
