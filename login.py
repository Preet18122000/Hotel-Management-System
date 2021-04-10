from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
from main import HotelManagementSystem


def main():
    main_window = Tk()
    app = LoginWindow(main_window)
    main_window.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Login")
        self.root.geometry("1550x800+0+0")


        bg = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\loginbg.webp")
        bg = bg.resize((1550, 800), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)
        labelbg = Label(self.root, image=self.photobg, bd=4, relief=RIDGE)
        labelbg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black", bd=4, relief=RIDGE)
        frame.place(x=610, y=150, width=340, height=450)

        login = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\login-removebg-preview.png")
        login = login.resize((100, 100), Image.ANTIALIAS)
        self.photologin = ImageTk.PhotoImage(login)
        labellogin = Label(self.root, image=self.photologin, bd=0, relief=RIDGE, bg="black")
        labellogin.place(x=730, y=155, width=100, height=100)

        getstart = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        getstart.place(x=95, y=100)

        username_icon = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\username-removebg-preview.png")
        username_icon = username_icon.resize((25, 25), Image.ANTIALIAS)
        self.photousername = ImageTk.PhotoImage(username_icon)
        labelusername = Label(self.root, image=self.photousername, bd=0, relief=RIDGE, bg="black")
        labelusername.place(x=650, y=310, width=25, height=25)
        username = Label(frame, text="Email Address", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username.place(x=65, y=155)
        self.username_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.username_entry.place(x=40, y=185, width=270)

        password_icon = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\password-removebg-preview.png")
        password_icon = password_icon.resize((25, 25), Image.ANTIALIAS)
        self.photopassword = ImageTk.PhotoImage(password_icon)
        labelpassword = Label(self.root, image=self.photopassword, bd=0, relief=RIDGE, bg="black")
        labelpassword.place(x=650, y=380, width=25, height=25)
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password.place(x=65, y=225)
        self.password_entry = ttk.Entry(frame,show="*", font=("times new roman", 15, "bold"))
        self.password_entry.place(x=40, y=255, width=270)

        # button
        loginbtn = Button(frame, text="Login", command=self.loginbtn, font=("times new roman", 16, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=120, y=300, width=100, height=40)

        regbtn = Button(frame, text="New Registration", command=self.reg_win, font=("times new roman", 12, "bold"), borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        regbtn.place(x=10, y=350, width=200)

        passwordbtn = Button(frame, text="Forgotten Password?", command=self.forgetwindow, font=("times new roman", 12, "bold"), borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        passwordbtn.place(x=20, y=375, width=200)

    def loginbtn(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                          database="management")
        cursor = connect.cursor()
        cursor.execute("select * from registration where email=%s and password=%s", (
            self.username_entry.get(),
            self.password_entry.get()
        ))
        row = cursor.fetchone()
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            if row == None:
                messagebox.showerror("Error", "Invalid Email and Password", parent=self.root)
            else:
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)
        connect.commit()
        connect.close()

    def reg_win(self):
        self.reg_window = Toplevel(self.root)
        self.app = Registration(self.reg_window)

    def reset_password(self):
        if self.sec_answer_entry.get() == "Select":
            messagebox.showerror("Error","Select Security Question", parent=self.reset_root)
        elif self.sec_ans.get() == "":
            messagebox.showerror("Error","Answer the Security Question", parent=self.reset_root)
        elif self.new_pass_entry == "":
            messagebox.showerror("Error","Please Enter your new password", parent=self.reset_root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            query = ("select * from registration where email=%s and secques=%s and secans=%s")
            value = (self.username_entry.get(), self.sec_answer_entry.get(), self.sec_ans.get())
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the correct answer", parent=self.reset_root)
            else:
                query = ("update registration set password=%s where email=%s")
                value = (self.new_pass_entry.get(), self.username_entry.get())
                cursor.execute(query, value)

                connect.commit()
                connect.close()
                messagebox.showinfo("Success", "Your password has been reset successfully", parent=self.reset_root)
                self.reset_root.destroy()

    def forgetwindow(self):
        if self.username_entry.get() == "":
            messagebox.showerror("Error", "Please Enter Email Address to reset password", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            query = ("select * from registration where email=%s")
            value = (self.username_entry.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter Valid Email Address to reset password", parent=self.root)
            else:
                connect.close()
                self.reset_root = Toplevel()
                self.reset_root.title("Forget Password")
                self.reset_root.geometry("340x450+610+170")

                resetframe = Frame(self.reset_root, bg="white")
                resetframe.place(x=0, y=0, width=340, height=450)

                lbl = Label(resetframe, text="Reset Password", font=("times new roman", 25, "bold"), bg="white", fg="red")
                lbl.place(x=0, y=10, relwidth=1, height= 40)

                sec_quest = Label(resetframe, text="Select Security Questions", font=("times new roman", 15, "bold"),
                                  bg="white")
                sec_quest.place(x=60, y=80)
                self.sec_answer_entry = ttk.Combobox(resetframe,
                                                font=("times new roman", 15, "bold"), state="readonly")
                self.sec_answer_entry["values"] = (
                "Select", "Your Birthplace", "Your favourite cuisine", "Your pet name", "Your favourite color")
                self.sec_answer_entry.current(0)
                self.sec_answer_entry.place(x=60, y=110, width=220)

                sec_ans = Label(resetframe, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                sec_ans.place(x=60, y=150)
                self.sec_ans = ttk.Entry(self.reset_root,  font=("times new roman", 15, "bold"))
                self.sec_ans.place(x=60, y=180, width=220)

                new_pass = Label(resetframe, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_pass.place(x=60, y=220)
                self.new_pass_entry = ttk.Entry(self.reset_root, show="*", font=("times new roman", 15, "bold"))
                self.new_pass_entry.place(x=60, y=250, width=220)

                resetbtn = Button(resetframe, command=self.reset_password, text="Reset", font=("times new roman", 15, "bold"), bg="green", fg="white")
                resetbtn.place(x=127, y=290, width=80, height=30)




class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Registration")
        self.root.geometry("1550x800+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_secques = StringVar()
        self.var_secans = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_cbtn = IntVar()


        bg = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\golden-coast-beach-hotel-0.jpg")
        bg = bg.resize((1550, 800))
        self.photobg = ImageTk.PhotoImage(bg)
        labelbg = Label(self.root, image=self.photobg, bd=4, relief=RIDGE)
        labelbg.place(x=0, y=0, relwidth=1, relheight=1)

        # frame
        frame = Frame(self.root, bg="white", relief=RIDGE)
        frame.place(x=270, y=150, width=1000, height=500)

        bg1 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\180725_The-Palace_Pool-photoshoot_16.webp")
        bg1 = bg1.resize((1000, 500))
        self.photobg1 = ImageTk.PhotoImage(bg1)
        labelbg1 = Label(frame, image=self.photobg1, bd=0, relief=RIDGE)
        labelbg1.place(x=0, y=0, width=450, height=500)

        reglabel = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        reglabel.place(x=460, y=0)

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=467, y=70)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=470, y=100, width=220)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=717, y=70)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname_entry.place(x=720, y=100, width=220)

        cno = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        cno.place(x=467, y=150)
        cno_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        cno_entry.place(x=470, y=180, width=220)

        email = Label(frame, text="Email Address", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=717, y=150)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email_entry.place(x=720, y=180, width=220)

        sec_quest = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white")
        sec_quest.place(x=467, y=230)
        sec_answer_entry = ttk.Combobox(frame, textvariable=self.var_secques, font=("times new roman", 15, "bold"), state="readonly")
        sec_answer_entry["values"] = ("Select", "Your Birthplace", "Your favourite cuisine", "Your pet name", "Your favourite color")
        sec_answer_entry.current(0)
        sec_answer_entry.place(x=470, y=260, width=220)

        sec_ans = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        sec_ans.place(x=717, y=230)
        sec_ans = ttk.Entry(frame, textvariable=self.var_secans, font=("times new roman", 15, "bold"))
        sec_ans.place(x=720, y=260, width=220)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=467, y=310)
        password_entry = ttk.Entry(frame,show="*", textvariable=self.var_password, font=("times new roman", 15, "bold"))
        password_entry.place(x=470, y=340, width=220)

        cpassword = Label(frame, text="Confirm Password",  font=("times new roman", 15, "bold"), bg="white")
        cpassword.place(x=717, y=310)
        cpassword_entry = ttk.Entry(frame,show="*", textvariable=self.var_cpassword, font=("times new roman", 15, "bold"))
        cpassword_entry.place(x=720, y=340, width=220)

        #   check
        checkbtn = Checkbutton(frame, variable=self.var_cbtn, text="I agree all the Terms & Conditions", font=("times new roman", 13, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=470, y=370)

        # image
        reg = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\registernow.jpg")
        reg = reg.resize((180, 40), Image.ANTIALIAS)
        self.photoreg = ImageTk.PhotoImage(reg)
        regbtn = Button(frame,command=self.addregistration, image=self.photoreg, bg="white", borderwidth=0, cursor="hand2")
        regbtn.place(x=470, y=418)

        loginnow = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\loginnow.jpg")
        loginnow = loginnow.resize((180, 40), Image.ANTIALIAS)
        self.photologin = ImageTk.PhotoImage(loginnow)
        loginbtn = Button(frame,command=self.loginwindow, image=self.photologin, bg="white", borderwidth=0, cursor="hand2")
        loginbtn.place(x=750, y=418)

    def addregistration(self):
        if self.var_fname.get() == ""  or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_secques.get() == "Select" or self.var_secans.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror("Error", "Password field does not match to each other", parent=self.root)
        elif self.var_cbtn.get() == 0:
            messagebox.showerror("Error", "Please agree terms and condition", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            query = ("select * from registration where contact=%s and email=%s")
            value = (self.var_contact.get(), self.var_email.get(),)
            cursor.execute(query, value)
            rows = cursor.fetchone()
            if rows != None:
                messagebox.showerror("Error", "User already exist, please try with another email or contact", parent=self.root)
            else:
                cursor.execute("insert into registration values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_secques.get(),
                    self.var_secans.get(),
                    self.var_password.get(),
                ))
                messagebox.showinfo("Success", "Registration completed successfully", parent=self.root)
                self.var_fname.set(""),
                self.var_lname.set(""),
                self.var_contact.set(""),
                self.var_email.set(""),
                self.var_secques.set(""),
                self.var_secans.set(""),
                self.var_password.set(""),
                self.var_cpassword.set(""),
                self.var_cbtn.set(0),
            connect.commit()
            connect.close()

    def loginwindow(self):
        self.root.destroy()




if __name__=="__main__":
    main()