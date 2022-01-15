from tkinter import *
from tkinter import messagebox

from administrative_window import administrative_window


def admin():
    def verify_admin():
        admin_id = admin_id_entry.get()
        admin_password = admin_password_entry.get()
        if admin_password != 'vasavi@1':
            messagebox.showwarning(title="please try again", message="Incorrect password/ admin_id")
        else:
            admin_login_window.destroy()
            administrative_window(admin_id)

    admin_login_window = Tk()
    admin_login_window.title("** ADMIN's LOGIN **")
    Label(admin_login_window, text="   ** ADMIN's LOGIN **   ", fg='indigo', font=("Wide Latin", 27),
          bg="grey").pack()
    admin_login_window.geometry("700x500")
    admin_id_label = Label(admin_login_window, text="Enter your admin-id : ", font=('Arial Rounded MT Bold', 12))
    admin_id_label.place(x=200, y=180)
    admin_password_label = Label(admin_login_window, text="Enter your password  :", font=('Arial Rounded MT Bold', 12))
    admin_password_label.place(x=200, y=230)
    admin_id_entry = Entry(admin_login_window, width=20, borderwidth=5)
    admin_id_entry.place(x=400, y=180)
    admin_password_entry = Entry(admin_login_window, width=20, borderwidth=5)
    admin_password_entry.place(x=400, y=230)
    verify_admin_button = Button(admin_login_window, text="Verify and Login", bg="Blue", activeforeground="Green",
                                 font=('Arial Rounded MT Bold', 12), command=verify_admin)
    verify_admin_button.place(x=100, y=280)
    exit_button = Button(admin_login_window, text="         EXIT         ", bg="red", activeforeground="Green",
                         font=('Arial Rounded MT Bold', 12), command=admin_login_window.destroy).place(x=550, y=280)
    admin_login_window.mainloop()
