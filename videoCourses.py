# importing webbrowser module
import webbrowser
# importing all files from tkinter module
from tkinter import *


def videoCourses():
    # creating root
    root = Tk()
    # setting GUI title
    root.title("Happy Learning"
               "")
    # setting GUI geometry
    root.geometry("750x500")

    # function to open CLanguage in browser
    def CLanguage():
        webbrowser.open("https://www.youtube.com/watch?v=87SH2Cn0s9A")

    # function to open python in browser
    def python():
        webbrowser.open("https://www.youtube.com/watch?v=_uQrJ0TkZlc")

    # function to open twitter in browser
    def cpp():
        webbrowser.open("https://www.youtube.com/watch?v=-LAa14DF9jM")

    # function to open youtube in browser
    def java():
        webbrowser.open("https://www.youtube.com/watch?v=xk4_1vDrzzo")

    # function to open whatsapp web in browser
    def mySQL():
        webbrowser.open("https://www.youtube.com/watch?v=zbMHLJ0dY4w")

    # function to open instagram in browser
    def webDev():
        webbrowser.open("https://www.youtube.com/watch?v=F5mRW0jo-U4")

    # function to open gmail in browser
    def dsa():
        webbrowser.open("https://www.youtube.com/watch?v=8hly31xKli0")

    Label(root, text="Click on the buttons to open video lectures", font="LUCIDA").pack()
    # creating button for each functions
    btn7 = Button(root, text="C language", command=CLanguage, font=('Arial Rounded MT Bold', 12),
                  bg='violet').pack(padx=4, pady=4)
    btn6 = Button(root, text="Python", command=python, font=('Arial Rounded MT Bold', 12), bg='violet').pack(
        padx=4, pady=4)
    btn5 = Button(root, text="C++ Tutorials", command=cpp, font=('Arial Rounded MT Bold', 12), bg='violet').pack(
        padx=4, pady=4)
    btn4 = Button(root, text="Java Tutorials", command=java, font=('Arial Rounded MT Bold', 12), bg='violet').pack(
        padx=4, pady=4)
    btn3 = Button(root, text="MySQL Tutorials", command=mySQL, font=('Arial Rounded MT Bold', 12),
                  bg='violet').pack(padx=4, pady=4)
    btn2 = Button(root, text="Web Development from Scratch", command=webDev, font=('Arial Rounded MT Bold', 12),
                  bg='violet').pack(padx=4, pady=4)
    btn1 = Button(root, text="DSA", command=dsa, font=('Arial Rounded MT Bold', 12), bg='violet').pack(padx=2,
                                                                                                       pady=4)

    # running the mainloop()
    root.mainloop()
