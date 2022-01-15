from tkinter import *
from tkinter import messagebox

from functionsPackage.courses import cse, ece, eee, mech, civil


def registerToCourse():
    courses_window = Tk()
    courses_window.title('  Courses Available  ')
    Label(courses_window, text="   **  Courses Available  **   ", fg='indigo', font=("Wide Latin", 27),
          bg="grey").pack()
    courses_window.geometry("700x500")
    option = IntVar()

    def display_specialized_courses():
        if option.get() == 1:
            courses_window.destroy()
            cse.display()
        elif option.get() == 2:
            courses_window.destroy()
            ece.display()
        elif option.get() == 3:
            courses_window.destroy()
            eee.display()
        elif option.get() == 4:
            courses_window.destroy()
            mech.display()
        elif option.get() == 5:
            courses_window.destroy()
            civil.display()
    R1_button = Radiobutton(courses_window, text="IT/CSE/CS/CST courses", variable=option, value=1,
                            font=('Arial Rounded MT Bold', 12), foreground="red", background="light green",
                            command=display_specialized_courses)
    R1_button.pack(anchor=CENTER, pady=4)

    R2_button = Radiobutton(courses_window, text="ECE courses", variable=option, value=2,
                            font=('Arial Rounded MT Bold', 12), foreground="indigo", background="light green",
                            command=display_specialized_courses)
    R2_button.pack(anchor=CENTER, pady=4)

    R3_button = Radiobutton(courses_window, text="EEE courses", variable=option, value=3,
                            font=('Arial Rounded MT Bold', 12), foreground="black", background="light green",
                            command=display_specialized_courses)
    R3_button.pack(anchor=CENTER, pady=4)

    R4_button = Radiobutton(courses_window, text="Mechanical Engineering courses", variable=option, value=4,
                            font=('Arial Rounded MT Bold', 12), foreground="blue", background="light green",
                            command=display_specialized_courses)
    R4_button.pack(anchor=CENTER, pady=4)

    R5_button = Radiobutton(courses_window, text="Civil Engineering courses", variable=option, value=5,
                            font=('Arial Rounded MT Bold', 12), foreground="purple", background="light green",
                            command=display_specialized_courses)
    R5_button.pack(anchor=CENTER, pady=4)
    # btn = Button(courses_window, text='back', command=welcomewindow).pack()
    messagebox.showinfo('Select Course To Register Into The course', " Click OK 🆗 To See the Course Structure")

    courses_window.mainloop()
