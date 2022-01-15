from tkinter import *
from tkinter import messagebox


def add_course():
    add_course_window = Tk()
    add_course_window.geometry("700x500")
    add_course_window.title("Add New Course")
    Label(add_course_window, text="**Add New Course**", fg='indigo', bg='grey', font=("Wide Latin", 27)).pack()
    option = IntVar()

    def add_course_to_database():
        read_details_of_new_course_window = Tk()
        read_details_of_new_course_window.geometry("900x500")
        read_details_of_new_course_window.title("Give details of New Course")
        Label(read_details_of_new_course_window, text="**Give details of New Course**", fg='indigo', bg='grey',
              font=("Wide Latin", 27)).pack()
        Label(read_details_of_new_course_window, text="Enter the name of course : ",
              font=('Arial Rounded MT Bold', 12)).place(x=200, y=160)
        Label(read_details_of_new_course_window, text="Enter tutor name :",
              font=('Arial Rounded MT Bold', 12)).place(x=200, y=200)
        Label(read_details_of_new_course_window, text="Enter course starting date :",
              font=('Arial Rounded MT Bold', 12)).place(x=200, y=240)
        Label(read_details_of_new_course_window, text="Enter course ending date :",
              font=('Arial Rounded MT Bold', 12)).place(x=200, y=280)
        Label(read_details_of_new_course_window, text="Enter course exam date :",
              font=('Arial Rounded MT Bold', 12)).place(x=200, y=320)
        new_course_name_entry = Entry(read_details_of_new_course_window, width=20, borderwidth=8)
        new_course_name_entry.place(x=500, y=160)
        new_course_tutor_name_entry = Entry(read_details_of_new_course_window, width=20, borderwidth=8)
        new_course_tutor_name_entry.place(x=500, y=200)
        new_course_starting_date_entry = Entry(read_details_of_new_course_window, width=20, borderwidth=8)
        new_course_starting_date_entry.place(x=500, y=240)
        new_course_ending_date_entry = Entry(read_details_of_new_course_window, width=20, borderwidth=8)
        new_course_ending_date_entry.place(x=500, y=280)
        new_course_exam_date_entry = Entry(read_details_of_new_course_window, width=20, borderwidth=8)
        new_course_exam_date_entry.place(x=500, y=320)

        def save():
            new_course_tutor_name = new_course_tutor_name_entry.get()
            new_course_name = new_course_name_entry.get()
            new_course_exam_date = new_course_exam_date_entry.get()
            new_course_starting_date = new_course_starting_date_entry.get()
            new_course_ending_date = new_course_ending_date_entry.get()
            with open('tutors.txt', 'a') as f:
                f.write('\n')
                f.write(new_course_tutor_name)

            with open('exam_date.txt', 'a') as f:
                f.write('\n')
                f.write(new_course_exam_date)

            with open('starting_date.txt', 'a') as f:
                f.write('\n')
                f.write(new_course_starting_date)

            with open('ending_date.txt', 'a') as f:
                f.write('\n')
                f.write(new_course_ending_date)

            if option.get() == 1:
                with open('cse_courses.txt', 'a') as f:
                    f.write('\n')
                    f.write(new_course_name)
            elif option.get() == 2:
                with open('ece_courses.txt', 'a') as f:
                    f.write('\n')
                    f.write(new_course_name)
            elif option.get() == 3:
                with open('eee_courses.txt', 'a') as f:
                    f.write('\n')
                    f.write(new_course_name)
            elif option.get() == 4:
                with open('mech_courses.txt', 'a') as f:
                    f.write('\n')
                    f.write(new_course_name)
            elif option.get() == 5:
                with open('civil_courses.txt', 'a') as f:
                    f.write('\n')
                    f.write(new_course_name)

            messagebox.showinfo('Added Successfully', "   Course Added Successfully   ")





        Button(read_details_of_new_course_window, text=" Save Details ", command=save,
               font=('Arial Rounded MT Bold', 12), bg='cyan', fg='black', activeforeground='green').place(x=170, y=400)
        Button(read_details_of_new_course_window, text="Exit", font=('Arial Rounded MT Bold', 12),
               command=read_details_of_new_course_window.destroy, bg='red', fg='black',
               activeforeground='red').place(x=650, y=400)
        read_details_of_new_course_window.mainloop()

    R1_button = Radiobutton(add_course_window, text="IT/CSE/CS/CST courses", variable=option, value=1,
                            font=('Arial Rounded MT Bold', 12), foreground="red", background="light blue",
                            command=add_course_to_database)
    R1_button.pack(anchor=CENTER, pady=4)

    R2_button = Radiobutton(add_course_window, text="ECE courses", variable=option, value=2,
                            font=('Arial Rounded MT Bold', 12), foreground="indigo", background="light blue",
                            command=add_course_to_database)
    R2_button.pack(anchor=CENTER, pady=4)

    R3_button = Radiobutton(add_course_window, text="EEE courses", variable=option, value=3,
                            font=('Arial Rounded MT Bold', 12), foreground="black", background="light blue",
                            command=add_course_to_database)
    R3_button.pack(anchor=CENTER, pady=4)

    R4_button = Radiobutton(add_course_window, text="Mechanical Engineering courses", variable=option, value=4,
                            font=('Arial Rounded MT Bold', 12), foreground="blue", background="light blue",
                            command=add_course_to_database)
    R4_button.pack(anchor=CENTER, pady=4)

    R5_button = Radiobutton(add_course_window, text="Civil Engineering courses", variable=option, value=5,
                            font=('Arial Rounded MT Bold', 12), foreground="purple", background="light blue",
                            command=add_course_to_database)
    R5_button.pack(anchor=CENTER, pady=4)
    Button(add_course_window, text="Log Out", font=('Arial Rounded MT Bold', 12),
           command=add_course_window.destroy, bg='red', fg='white',
           activeforeground='red').pack(anchor=CENTER, pady=4)
    add_course_window.mainloop()
