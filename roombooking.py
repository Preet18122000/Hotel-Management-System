from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+230+220")

        #  varialbles
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subltotal = StringVar()
        self.var_total = StringVar()


        # ----------------- Heading and logo ------------------------
        labeltitle = Label(self.root, text="ROOM BOOKING PANEL", font=("times new roman", 18, "bold"), bd=2, fg="white", bg="black", relief=RIDGE)
        labeltitle.place(x=5, y=0, width=1295, height=50)

        img1 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotellogo.jpg")
        img1 = img1.resize((120, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)
        labelimglogo = Label(self.root, image=self.photoimg, bd=0, relief=RIDGE)
        labelimglogo.place(x=5, y=0, width=100, height=50)

        #  ------------------Label Frame Left -----------------------------------------
        labelframeleft = LabelFrame(self.root, text="Room Booking Details", font=("times new roman", 18, "bold"), bd=2, relief=RIDGE, padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=520)

        # -------------------Label and Entry --------------------------
        #customer contact
        cust_contact = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Customer Contact")
        cust_contact.grid(row=0, column=0, sticky=W)
        contact_entry = ttk.Entry(labelframeleft, textvariable=self.var_contact,font=("times new roman",13,"bold"), width=20)
        contact_entry.grid(row=0 , column=1, sticky=W)
        fetch_customer_detail = Button(labelframeleft, command=self.fetccontanct, text="Fetch Data", font=("times new roman",10,"bold"), fg="white", bg="black", width=8)
        fetch_customer_detail.place(x=325, y=3)

        #check in
        checkin = Label(labelframeleft,  font=("times new roman",12,"bold"), padx=2, pady=6, text="Check In Date")
        checkin.grid(row=1, column=0, sticky=W)
        checkin_entry = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("times new roman",13,"bold"), width=29)
        checkin_entry.grid(row=1, column=1)

        #check out
        checkout = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Check Out Date")
        checkout.grid(row=2, column=0, sticky=W)
        checkout_entry = ttk.Entry(labelframeleft,textvariable=self.var_checkout, font=("times new roman",13,"bold"), width=29)
        checkout_entry.grid(row=2, column=1)

        #room type
        roomtype = Label(labelframeleft, font=("times new roman", 12, "bold"), padx=2, pady=6, text="Room Type")
        roomtype.grid(row=3, column=0, sticky=W)
        roomtype_entry = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("times new roman", 13, "bold"), width=27, state="readonly")
        roomtype_entry["value"] = ("Single Bed", "Double Bed", "Royal Suite", "Luxury Suite", "Honeymoon Suite")
        roomtype_entry.current(0)
        roomtype_entry.grid(row=3, column=1)

        # Available
        available = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Available Room")
        available.grid(row=4, column=0, sticky=W)
        # available_entry = ttk.Entry(labelframeleft, textvariable=self.var_roomno, font=("times new roman",13,"bold"), width=29)
        # available_entry.grid(row=4, column=1)
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                          database="management")
        cursor = connect.cursor()
        cursor.execute("select roomno from rdetails")
        rows = cursor.fetchall()
        available_entry = ttk.Combobox(labelframeleft,textvariable=self.var_roomno, font=("times new roman", 13, "bold"), width=27, state="readonly")
        available_entry["value"] = rows
        available_entry.current(0)
        available_entry.grid(row=4, column=1)

        #meal
        meal = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Meal")
        meal.grid(row=5, column=0, sticky=W)
        meal_entry = ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("times new roman",13,"bold"), width=29)
        meal_entry.grid(row=5, column=1)

        #No of Days
        noofdays = Label(labelframeleft,font=("times new roman",12,"bold"), padx=2, pady=6, text="No of Days")
        noofdays.grid(row=6, column=0, sticky=W)
        noofdays_entry = ttk.Entry(labelframeleft,textvariable=self.var_noofdays,  font=("times new roman",13,"bold"), width=29)
        noofdays_entry.grid(row=6, column=1)

        #Paid Tax
        paidtax = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Paid Tax")
        paidtax.grid(row=7, column=0, sticky=W)
        paidtax_entry = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("times new roman",13,"bold"), width=29)
        paidtax_entry.grid(row=7, column=1)

        #Sub Total
        subtotal = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Sub Total")
        subtotal.grid(row=8, column=0, sticky=W)
        subtotal_entry = ttk.Entry(labelframeleft,textvariable=self.var_subltotal, font=("times new roman",13,"bold"), width=29)
        subtotal_entry.grid(row=8, column=1)

        #Total cost
        totalcost = Label(labelframeleft, font=("times new roman",12,"bold"), padx=2, pady=6, text="Total Cost")
        totalcost.grid(row=9, column=0, sticky=W)
        totalcost_entry = ttk.Entry(labelframeleft,textvariable=self.var_total, font=("times new roman",13,"bold"), width=29)
        totalcost_entry.grid(row=9, column=1)

        # -------------------Bill Button ------------------
        billbtn = Button(labelframeleft, text="Bill",command=self.total, font=("times new roman", 12, "bold"), bg="black", fg="white",width=10)
        billbtn.grid(row=10, column=0, padx=1, sticky=W)

        # ------------------ Button Frame ---------------------
        buttonframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        buttonframe.place(x=0, y=400, width=417, height=37)

        addbtn = Button(buttonframe, text="SAVE", command=self.addbtn, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        addbtn.grid(row=0, column=0, padx=2)

        deletebtn = Button(buttonframe,  text="DELETE", command=self.delete, font=("times new roman", 12, "bold"),bg="black", fg="white", width=10)
        deletebtn.grid(row=0, column=2, padx=2)

        updatebtn = Button(buttonframe, text="UPDATE",command=self.update, font=("times new roman", 12, "bold"),bg="black", fg="white", width=10)
        updatebtn.grid(row=0, column=1, padx=2)

        resetbtn = Button(buttonframe, text="RESET", command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        resetbtn.grid(row=0, column=3, padx=2)

    # ----------------- Image --------------------
        img2 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotelroom.jpg")
        img2 = img2.resize((500, 300), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        labelimgroom = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        labelimgroom.place(x=760, y=55, width=500, height=300)

    # -------------------------- search system ---------------------------
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=435, y=280, width=860, height=290)

        labelsearchby = Label(tableframe, font=("times new roman", 12, "bold"), text="Search By", bg="red", fg="white")
        labelsearchby.grid(row=0, column=0, sticky=W, padx=2)

        combosearchby = ttk.Combobox(tableframe, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combosearchby["value"] = ("Room Number")
        combosearchby.current(0)
        combosearchby.grid(row=0, column=1, padx=2)

        self.entry_var = StringVar()
        searchentry = ttk.Entry(tableframe, textvariable=self.entry_var, font=("times new roman", 13, "bold"), width=29)
        searchentry.grid(row=0, column=2, padx=2)

        searchbtn = Button(tableframe, text="Search", command=self.search,  font=("times new roman", 11, "bold"), bg="black", fg="white", width=10)
        searchbtn.grid(row=0, column=3, padx=2)

        showbtn = Button(tableframe, text="Show All", command=self.data_display, font=("times new roman", 11, "bold"), bg="black", fg="white", width=10)
        showbtn.grid(row=0, column=4, padx=2)

        # show data table
        displayframe = Frame(tableframe, bd=2, relief=RIDGE)
        displayframe.place(x=0, y=50, width=860, height=180)

        xscroll = Scrollbar(displayframe, orient=HORIZONTAL)
        yscroll = Scrollbar(displayframe, orient=VERTICAL)

        self.roombookingtable = ttk.Treeview(displayframe, column=("contact", "checkin", "checkout", "roomtype", "availability", "meal", "noofdays"),
                                             xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.roombookingtable.xview)
        yscroll.config(command=self.roombookingtable.yview)

        self.roombookingtable.heading("contact", text="Contact No")
        self.roombookingtable.heading("checkin", text="Check In")
        self.roombookingtable.heading("checkout", text="Check Out")
        self.roombookingtable.heading("roomtype", text="Room Type")
        self.roombookingtable.heading("availability", text="Room No")
        self.roombookingtable.heading("meal", text="Meal")
        self.roombookingtable.heading("noofdays", text="No of Days")

        self.roombookingtable["show"]="headings"

        self.roombookingtable.column("contact", width=100)
        self.roombookingtable.column("checkin", width=100)
        self.roombookingtable.column("checkout", width=100)
        self.roombookingtable.column("roomtype", width=100)
        self.roombookingtable.column("availability", width=100)
        self.roombookingtable.column("meal", width=100)
        self.roombookingtable.column("noofdays", width=100)

        self.roombookingtable.pack(fill=BOTH, expand=1)
        self.roombookingtable.bind("<ButtonRelease-1>", self.get_cursor)
        self.data_display()

    # --------------------------- Add Button -----------------
    def addbtn(self):
        if self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == "" or self.var_roomno.get() == "" or self.var_meal.get() == ""\
                or self.var_noofdays.get()== "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                cursor.execute("insert into roombook values(%s, %s, %s, %s, %s, %s, %s)", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
                ))
                connect.commit()
                self.data_display()
                connect.close()
                messagebox.showinfo("Success", "Room has been added", parent=self.root)
            except EXCEPTION as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)

    def data_display(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                          database="management")
        cursor = connect.cursor()
        cursor.execute("select * from roombook")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.roombookingtable.delete(*self.roombookingtable.get_children())
            for i in rows:
                self.roombookingtable.insert("", END, values=i)
            connect.commit()
        connect.close()

    def get_cursor(self, events=""):
        cursor_data = self.roombookingtable.focus()
        content = self.roombookingtable.item(cursor_data)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomno.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == "" or self.var_roomno.get() == "" or self.var_meal.get() == ""\
                or self.var_noofdays.get()== "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            cursor.execute("update roombook set contact=%s, checkin=%s, checkout=%s, roomtype=%s, meal=%s, noofdays=%s where roomavail=%s", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_roomno.get(),
            ))
            connect.commit()
            self.data_display()
            connect.close()
            messagebox.showinfo("Success", "Data has been updated", parent=self.root)

    def delete(self):
        yesno = messagebox.askyesno("Hotel Management System", "Do you want to delete this detail", parent=self.root)
        if yesno > 0:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            query = "delete from roombook where contact=%s"
            value = (self.var_contact.get(),)
            cursor.execute(query, value)
            connect.commit()
            self.data_display()
            connect.close()
        else:
            if not yesno:
                return

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomno.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subltotal.set("")
        self.var_total.set("")

    def fetccontanct(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please, Enter contact number", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
            cursor = connect.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            cursor.execute(query, value)
            rows = cursor.fetchone()
            if rows == None:
                messagebox.showerror("Error", "This number is not found", parent=self.root)
            else:
                connect.commit()
                connect.close()

                showdataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showdataframe.place(x=445, y=55, width=300, height=200)

                # name
                labelname = Label(showdataframe, text="Name:", font=("times new roman", 12, "bold"))
                labelname.place(x=0, y=0)
                lblname = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lblname.place(x=90, y=0)

                # gender
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cursor.execute(query, value)
                rows = cursor.fetchone()

                labelgender = Label(showdataframe, text="Gender:", font=("times new roman", 12, "bold"))
                labelgender.place(x=0, y=30)
                lblgender = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lblgender.place(x=90, y=30)

                #  email
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                query = ("select email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cursor.execute(query, value)
                rows = cursor.fetchone()

                labelemail = Label(showdataframe, text="Email:", font=("times new roman", 12, "bold"))
                labelemail.place(x=0, y=60)
                lblemail = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lblemail.place(x=90, y=60)

                # Nationality
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cursor.execute(query, value)
                rows = cursor.fetchone()

                labelnation = Label(showdataframe, text="Nationality:", font=("times new roman", 12, "bold"))
                labelnation.place(x=0, y=90)
                lblnation = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lblnation.place(x=90, y=90)

            # Address
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cursor.execute(query, value)
                rows = cursor.fetchone()

                labeladdress = Label(showdataframe, text="Address:", font=("times new roman", 12, "bold"))
                labeladdress.place(x=0, y=120)
                lbladdress = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lbladdress.place(x=90, y=120)

            # id proof
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                query = ("select Idproof from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cursor.execute(query, value)
                rows = cursor.fetchone()

                labelid = Label(showdataframe, text="Id Proof:", font=("times new roman", 12, "bold"))
                labelid.place(x=0, y=150)
                lblid = Label(showdataframe, text=rows, font=("times new roman", 12, "bold"))
                lblid.place(x=90, y=150)

    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkout.get()
        indate = datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)

        meal_cost = {
            "breakfast":100,
            "lunch":300,
            "dinner":300,
            "breakfast lunch": 350,
            "breakfast dinner": 350,
            "lunch dinner": 500,
            "breakfast lunch dinner": 600
        }
        room_cost = {
            "single bed": 500,
            "double bed": 800,
            "royal suite": 2000,
            "luxury suite": 1500,
            "honeymoon suite": 1500
        }
        if self.var_meal.get().lower() in meal_cost and self.var_roomtype.get().lower() in room_cost:
            meal = float(meal_cost[self.var_meal.get().lower()])
            room  = float(room_cost[self.var_roomtype.get().lower()])
            days = float(self.var_noofdays.get())
            temp = float(meal+room)
            subt = float(temp*days)
            tax = f"Rs. {str(subt*0.18)}"
            st = f"Rs. {str(subt)}"
            tt = f"Rs. {str(subt*0.18+subt)}"
            self.var_paidtax.set(tax)
            self.var_subltotal.set(st)
            self.var_total.set(tt)

    def search(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
        cursor = connect.cursor()
        cursor.execute("select * from roombook where roomavail=" + str(self.entry_var.get()))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.roombookingtable.delete(*self.roombookingtable.get_children())
            for i in rows:
                self.roombookingtable.insert("", END, values=i)
            connect.commit()
        connect.close()


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()