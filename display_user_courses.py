import random
from tkinter import *

course_list = []
with open('cse_courses.txt', 'r') as f0:
    l0 = f0.readlines()

with open('ece_courses.txt', 'r') as f1:
    l1 = f1.readlines()

with open('eee_courses.txt', 'r') as f2:
    l2 = f2.readlines()

with open('mech_courses.txt', 'r') as f3:
    l3 = f3.readlines()

with open('civil_courses.txt', 'r') as f4:
    l4 = f4.readlines()

for i in l0:
    course_list.append(i.strip())

for i in l1:
    course_list.append(i.strip())

for i in l2:
    course_list.append(i.strip())

for i in l3:
    course_list.append(i.strip())

for i in l4:
    course_list.append(i.strip())

course1 = random.randint(0, len(course_list)-1)
course2 = random.randint(0, len(course_list)-1)
course3 = random.randint(0, len(course_list)-1)
course4 = random.randint(0, len(course_list)-1)
course5 = random.randint(0, len(course_list)-1)


def display_user_courses():
    display_user_courses_window = Tk()
    display_user_courses_window.geometry('750x500')
    display_user_courses_window.title("Your Courses")
    Label(display_user_courses_window, text='All the courses you have' + '\n' + 'registered in :', fg='indigo',
          font=("Wide Latin", 27), bg="grey").pack()
    Label(display_user_courses_window, text=course_list[course1],
          font=('Arial Rounded MT Bold', 12), foreground="light blue", background="blue").pack(pady=4)
    Label(display_user_courses_window, text=course_list[course2],
          font=('Arial Rounded MT Bold', 12), foreground="light blue", background="blue").pack(pady=4)
    Label(display_user_courses_window, text=course_list[course3],
          font=('Arial Rounded MT Bold', 12), foreground="light blue", background="blue").pack(pady=4)
    Label(display_user_courses_window, text=course_list[course4],
          font=('Arial Rounded MT Bold', 12), foreground="light blue", background="blue").pack(pady=4)
    Label(display_user_courses_window, text=course_list[course5],
          font=('Arial Rounded MT Bold', 12), foreground="light blue", background="blue").pack(pady=4)
    Button(display_user_courses_window, text='back', command=display_user_courses_window.destroy,
           font=('Arial Rounded MT Bold', 12), foreground="purple", background="violet").pack(pady=6)
    display_user_courses_window.mainloop()


# display_user_courses()
