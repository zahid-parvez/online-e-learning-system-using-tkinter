from tkinter import *

_list = []


def remove_course():
    def remove():
        def delete():
            if option.get() == 1:
                file_name = 'cse_courses.txt'
            elif option.get() == 2:
                file_name = 'ece_courses.txt'
            elif option.get() == 3:
                file_name = 'eee_courses.txt'
            elif option.get() == 4:
                file_name = 'mech_courses.txt'
            elif option.get() == 5:
                file_name = 'civil_courses.txt'

            with open(file_name, 'r') as f:
                list1 = f.readlines()

            for j in list1:
                _list.append(j.strip())

            if course_name.get() in _list:
                _list.remove(course_name.get())

            with open(file_name, 'w') as f:
                for i in _list:
                    f.write(i + '\n')

        Label(remove_course_window, text='enter course name to remove : ', font=('Arial Rounded MT Bold', 12),
              fg='green').pack(anchor=W, pady=4)
        course_name = Entry(remove_course_window, width=20, borderwidth=4)
        course_name.pack(anchor=W, pady=4)
        Button(remove_course_window, text='delete', command=delete).pack(anchor=CENTER, pady=4)

    remove_course_window = Tk()
    remove_course_window.title("Remove Course Window")
    option = IntVar()
    Label(remove_course_window, text="** Remove Course **", fg='indigo', font=("Wide Latin", 27),
          bg="grey").pack()
    remove_course_window.geometry("800x500")
    R1_button = Radiobutton(remove_course_window, text="IT/CSE/CS/CST courses", variable=option, value=1,
                            font=('Arial Rounded MT Bold', 12), foreground="red", background="light blue",
                            command=remove)
    R1_button.pack(anchor=CENTER, pady=4)

    R2_button = Radiobutton(remove_course_window, text="ECE courses", variable=option, value=2,
                            font=('Arial Rounded MT Bold', 12), foreground="indigo", background="light blue",
                            command=remove)
    R2_button.pack(anchor=CENTER, pady=4)

    R3_button = Radiobutton(remove_course_window, text="EEE courses", variable=option, value=3,
                            font=('Arial Rounded MT Bold', 12), foreground="black", background="light blue",
                            command=remove)
    R3_button.pack(anchor=CENTER, pady=4)

    R4_button = Radiobutton(remove_course_window, text="Mechanical Engineering courses", variable=option, value=4,
                            font=('Arial Rounded MT Bold', 12), foreground="blue", background="light blue",
                            command=remove)
    R4_button.pack(anchor=CENTER, pady=4)

    R5_button = Radiobutton(remove_course_window, text="Civil Engineering courses", variable=option, value=5,
                            font=('Arial Rounded MT Bold', 12), foreground="purple", background="light blue",
                            command=remove)
    R5_button.pack(anchor=CENTER, pady=4)
    Button(remove_course_window, text="Log Out", font=('Arial Rounded MT Bold', 12),
           command=remove_course_window.destroy, bg='red', fg='white',
           activeforeground='red').pack(anchor=CENTER, pady=4)
    remove_course_window.mainloop()
