import random
from tkinter import *

import welcomewindow

cse_list = []
with open('cse_courses.txt') as f:
    _list = f.readlines()

for j in _list:
    cse_list.append(j.strip())

tutors_list = []
with open('tutors.txt') as f:
    _list = f.readlines()

for j in _list:
    tutors_list.append(j.strip())


date_list = []
with open('starting_date.txt') as f:
    _list = f.readlines()

for j in _list:
    date_list.append(j.strip())


end_date_list = []
with open('ending_date.txt') as f:
    _list = f.readlines()

for j in _list:
    end_date_list.append(j.strip())


exam_date_list = []
with open('exam_date.txt') as f:
    _list = f.readlines()

for j in _list:
    exam_date_list.append(j.strip())


s = random.randint(0, len(tutors_list) - 1)
d = random.randint(0, len(date_list) - 1)
d1 = random.randint(0, len(end_date_list) - 1)
d2 = random.randint(0, len(end_date_list) - 1)
sir = tutors_list[s]
date = date_list[d]
date_1 = end_date_list[d1]
exam_date = exam_date_list[d2]
exam_mode_selection = random.randint(0, 100000)
if exam_mode_selection % 2 == 0:
    exam_mode = "Offline"
else:
    exam_mode = "Online"


def display():
    def course_structure():
        def driver_course_structure_widge():
            course_structure_widge.destroy()
            welcomewindow.welcomewindow()
        cse_courses_widge.destroy()
        course_structure_widge = Tk()
        course_structure_widge.title("Details")
        Label(course_structure_widge, text="   ** Course Details **   ", fg='indigo', font=("Wide Latin", 27),
              bg="grey").pack()
        course_structure_widge.geometry("700x500")
        Label(course_structure_widge, text=f"Course Starting Date   :   {date}", bg="blue", fg="white",
              font=('Arial Rounded MT Bold', 12)).pack(pady=6)
        Label(course_structure_widge, text=f"Tutorial By : {sir}", bg="orange", fg="white",
              font=('Arial Rounded MT Bold', 12)).pack(pady=6)
        Label(course_structure_widge, text=f"Course Ending Date     :   {date_1}", bg="green", fg="white",
              font=('Arial Rounded MT Bold', 12)).pack(pady=6)
        Label(course_structure_widge, text=f"Course Examination Date     :   {exam_date}", bg="pink", fg="black",
              font=('Arial Rounded MT Bold', 12)).pack(pady=6)
        Label(course_structure_widge, text=f"Course Examination Mode     :   {exam_mode}", bg="Yellow",
              fg="black", font=('Arial Rounded MT Bold', 12)).pack(pady=6)
        exit_button = Button(course_structure_widge, text="Exit ❌ ", bg="gray", fg="red",
                             font=('Arial Rounded MT Bold', 12), command=driver_course_structure_widge)
        exit_button.pack(pady=4)

        course_structure_widge.mainloop()

    values = list(range(1, len(cse_list) + 1))
    cse_courses_widge = Tk()
    cse_courses_widge.title("CSE/IT/CSE/CSIT courses")
    cse_courses_widge.geometry("750x500")
    Label(cse_courses_widge, text="   ** CSE/IT/CSE courses **   ", fg='indigo', font=("Wide Latin", 27),
          bg="grey").pack()
    option = IntVar()
    for course, i in zip(cse_list, values):
        Radiobutton(cse_courses_widge, text=course, variable=option, value=i, foreground="green",
                    bg="violet", font=('Arial Rounded MT Bold', 11)).pack(pady=4)
    selection_button = Button(cse_courses_widge, text="next⏭︎", bg="gray", fg="purple",
                              font=('Arial Rounded MT Bold', 12), command=course_structure)
    selection_button.pack()
    cse_courses_widge.mainloop()
