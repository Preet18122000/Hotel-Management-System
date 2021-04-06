from tkinter import *
from PIL import Image, ImageTk


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ------------------- Top image -----------------
        img1 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)   #  Antialias - convert high quality to low quality
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimg = Label(self.root, image = self.photoimg1, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=1550, height=140)

        # --------------------Logo Image -------------------
        img2 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotellogo.jpg")
        img2 = img2.resize((270, 140), Image.ANTIALIAS)   #  Antialias - convert high quality to low quality
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimglogo = Label(self.root, image = self.photoimg2, relief=RIDGE)
        labelimglogo.place(x=0, y=0, width=210, height=140)

        #  ------------------- Title ---------------------
        labeltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"),
                           bg="black", fg="white", bd=4, relief=RIDGE)
        labeltitle.place(x=0, y=140, width=1550, height=50)

        #  ------------------- Main Frame ----------------
        mainframe = Frame(self.root, bd=4, relief=RIDGE)
        mainframe.place(x=0, y=190, width=1550, height=620)

        #  ------------------- Menu inside main frame ----------------------
        labelmenu = Label(mainframe, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        labelmenu.place(x=0, y=0, width=230)

        # --------------------Btn frame inside main frame ----------------------
        btnframe = Frame(mainframe, bd=4, relief=RIDGE)
        btnframe.place(x=0, y=35, width=228, height=210)

        custbtn = Button(btnframe, text="CUSTOMER", width=20, font=("times new roman", 14, "bold"), bg="black", fg="white", cursor="hand2")
        custbtn.grid(row=0, column=0, pady=1)   #  customer detail

        roombtn = Button(btnframe, text="ROOM", width=20, font=("times new roman", 14, "bold"), bg="black", fg="white", cursor="hand2")
        roombtn.grid(row=1, column=0, pady=1)  #  room detail

        detailsbtn = Button(btnframe, text="DETAILS", width=20, font=("times new roman", 14, "bold"), bg="black", fg="white", cursor="hand2")
        detailsbtn.grid(row=2, column=0, pady=1)  #  detail btn

        reportbtn = Button(btnframe, text="REPORT", width=20, font=("times new roman", 14, "bold"), bg="black", fg="white", cursor="hand2")
        reportbtn.grid(row=3, column=0, pady=1)  # Report btn

        logoutbtn = Button(btnframe, text="LOGOUT", width=20, font=("times new roman", 14, "bold"), bg="black", fg="white", cursor="hand2")
        logoutbtn.grid(row=4, column=0, pady=1)  #logoutbtn

        # --------------------Reception Image ----------------
        img3 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\reception.jpeg")
        img3 = img3.resize((1295, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelimgreception = Label(mainframe, image = self.photoimg3, bd=4, relief=RIDGE)
        labelimgreception.place(x=230, y=0, width=1295, height=595)

        # -------------------left down ---------------------
        img4 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\left_down_hotel.jpg")
        img4 = img4.resize((228, 170), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        labelimgdownimg = Label(mainframe, image=self.photoimg4, bd=4, relief=RIDGE)
        labelimgdownimg.place(x=0, y=245, width=228, height=175)

        img5 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\food_left_down.jpg")
        img5 = img5.resize((228, 170), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        labelimgfood = Label(mainframe, image=self.photoimg5, bd=4, relief=RIDGE)
        labelimgfood.place(x=0, y=420, width=228, height=175)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
