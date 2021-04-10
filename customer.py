from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+230+220")

        #  --------------------- variables -----------------------
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_lname = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_email = StringVar()

        #  ----------------- Title --------------
        labeltitle = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"), bd=2, fg="white", bg="black", relief=RIDGE)
        labeltitle.place(x=0, y=0, width=1295, height=50)

        #  ----------------- Logo ---------------
        img1 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotellogo.jpg")
        img1 = img1.resize((120, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        labelimglogo = Label(self.root, image=self.photoimage1, relief=RIDGE, bd=0)
        labelimglogo.place(x=5, y=2, width=100, height=50)

        # ------------------ Label Frame --------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("times new roman",12,"bold"))
        labelframeleft.place(x=5, y=50, width=425, height=520)

        # ------------------Label and Entry ---------------
        # Customer Reference
        customer_reference = Label(labelframeleft, text="Customer Ref:", font=("times new roman",12,"bold"), padx=2, pady=6)
        customer_reference.grid(row=0, column=0, sticky=W)
        entry_customer_reference = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29,font=("times new roman",13,"bold"), state="readonly")
        entry_customer_reference.grid(row=0, column=1)

        #Customer Name
        customer_name = Label(labelframeleft, text="Customer Name:", font=("times new roman",12,"bold"), padx=2, pady=6)
        customer_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(labelframeleft, textvariable=self.var_name, width=29,font=("times new roman",13,"bold"))
        entry_name.grid(row=1, column=1)

        # Sur Name
        customer_lastname = Label(labelframeleft, text="Last Name:", font=("times new roman",12,"bold"), padx=2, pady=6)
        customer_lastname.grid(row=2, column=0, sticky=W)
        entry_lastname = ttk.Entry(labelframeleft, textvariable=self.var_lname, width=29,font=("times new roman",13,"bold"))
        entry_lastname.grid(row=2, column=1)

        # gender combobox
        customer_gender = Label(labelframeleft,text="Gender:", font=("times new roman",12,"bold"), padx=2, pady=6)
        customer_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender , font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        customer_postcode = Label(labelframeleft, text="Postcode:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        customer_postcode.grid(row=4, column=0, sticky=W)
        entry_postcode = ttk.Entry(labelframeleft, textvariable=self.var_postcode, width=29, font=("times new roman", 13, "bold"))
        entry_postcode.grid(row=4, column=1)

        # mobile Number
        customer_mnum = Label(labelframeleft, text="Mobile Number:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        customer_mnum.grid(row=5, column=0, sticky=W)
        entry_mnum = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("times new roman", 13, "bold"))
        entry_mnum.grid(row=5, column=1)


        #nationality
        customer_nationality = Label(labelframeleft, text="Nationality:",font=("times new roman", 12, "bold"), padx=2, pady=6)
        customer_nationality.grid(row=6, column=0, sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("Indian", "American", "EU resident", "Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=6, column=1)

        #idproof combobox
        customer_idproof = Label(labelframeleft, text="Id Proof Type:",font=("times new roman", 12, "bold"), padx=2, pady=6)
        customer_idproof.grid(row=7, column=0, sticky=W)
        combo_idproof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_idproof["value"] = ("Passport", "PAN Card", "Aadhaar Card", "Voter Id Card", "Driving License", "Other")
        combo_idproof.current(0)
        combo_idproof.grid(row=7, column=1)

        #id number
        customer_idnumber = Label(labelframeleft, text="Id Number:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        customer_idnumber.grid(row=8, column=0, sticky=W)
        entry_idnumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("times new roman", 13, "bold"))
        entry_idnumber.grid(row=8, column=1)

        # address
        customer_address = Label(labelframeleft, text="Customer Address:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        customer_address.grid(row=9, column=0, sticky=W)
        entry_address = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("times new roman", 13, "bold"))
        entry_address.grid(row=9, column=1)

        #mail
        customer_mail = Label(labelframeleft, text="Email Address:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        customer_mail.grid(row=10, column=0, sticky=W)
        entry_mail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_mail.grid(row=10, column=1)

        # ADD UPDATE DELETE RESET BUTTON
        buttonframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        buttonframe.place(x=0, y=400, width=417, height=37)

        addbtn = Button(buttonframe, text="ADD", command=self.addbtn, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        addbtn.grid(row=0, column=0, padx=2)

        deletebtn = Button(buttonframe, command=self.delete, text="DELETE", font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        deletebtn.grid(row=0, column=2, padx=2)

        updatebtn = Button(buttonframe, text="UPDATE", command=self.update, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        updatebtn.grid(row=0, column=1, padx=2)

        resetbtn = Button(buttonframe, text="RESET", command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        resetbtn.grid(row=0, column=3, padx=2)

        # -------------------------------------------  TABLE FRAME ---------------------------------------
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=435, y=50, width=860, height=520)

        labelsearchby = Label(tableframe, font=("times new roman", 12, "bold"), text="Search By", bg="red", fg="white")
        labelsearchby.grid(row=0, column=0, sticky=W, padx=2)

        combosearchby = ttk.Combobox(tableframe, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combosearchby["value"] = ("Reference Number",)
        combosearchby.current(0)
        combosearchby.grid(row=0, column=1, padx=2)

        self.entry_var = StringVar()
        searchentry = ttk.Entry(tableframe, textvariable=self.entry_var, font=("times new roman", 13, "bold"), width=29)
        searchentry.grid(row=0, column=2, padx=2)

        searchbtn = Button(tableframe, text="Search", command=self.search, font=("times new roman", 11, "bold"), bg="black", fg="white", width=10)
        searchbtn.grid(row=0, column=3, padx=2)

        showbtn = Button(tableframe, text="Show All", command=self.fetch_data, font=("times new roman", 11, "bold"), bg="black", fg="white", width=10)
        showbtn.grid(row=0, column=4, padx=2)

        # -------------- Show data table ------------------
        displayframe = Frame(tableframe, bd=2, relief=RIDGE)
        displayframe.place(x=0, y=50, width=860, height=360)

        scroll_x = ttk.Scrollbar(displayframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(displayframe, orient=VERTICAL)

        self.customer_details_table = ttk.Treeview(displayframe, column=("ref", "name", "lastname","gender","post","mobile", "nationality", "idproof",
                                                                         "idnumber", "address","email",), xscrollcommand=scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_details_table.xview)
        scroll_y.config(command=self.customer_details_table.yview)

        self.customer_details_table.heading("ref", text="Reference No")
        self.customer_details_table.heading("name", text="First Name")
        self.customer_details_table.heading("lastname", text="Last Name")
        self.customer_details_table.heading("gender", text="Gender")
        self.customer_details_table.heading("post", text="Postal Code")
        self.customer_details_table.heading("mobile", text="Mobile No")
        self.customer_details_table.heading("email", text="Email Address")
        self.customer_details_table.heading("nationality", text="Nationality")
        self.customer_details_table.heading("idproof", text="Id Proof")
        self.customer_details_table.heading("idnumber", text="Id No")
        self.customer_details_table.heading("address", text="Resident Address")

        self.customer_details_table["show"] = "headings"

        self.customer_details_table.column("ref", width=100)
        self.customer_details_table.column("name", width=100)
        self.customer_details_table.column("lastname", width=100)
        self.customer_details_table.column("gender", width=100)
        self.customer_details_table.column("post", width=100)
        self.customer_details_table.column("mobile", width=100)
        self.customer_details_table.column("email", width=100)
        self.customer_details_table.column("nationality", width=100)
        self.customer_details_table.column("idproof", width=100)
        self.customer_details_table.column("idnumber", width=100)
        self.customer_details_table.column("address", width=100)

        self.customer_details_table.pack(fill=BOTH, expand=1)
        self.customer_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def addbtn(self):
        if self.var_mobile.get() == "" or self.var_id_number.get() == "" or self.var_name.get() == "" or self.var_lname.get() == "" or self.var_gender.get() ==  ""\
                or self.var_postcode.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "" or self.var_id_proof.get() == "" \
                or self.var_address.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
                cursor = connect.cursor()
                cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_ref.get(),
                                                                                                 self.var_name.get(),
                                                                                                 self.var_lname.get(),
                                                                                                 self.var_gender.get(),
                                                                                                 self.var_postcode.get(),
                                                                                                 self.var_mobile.get(),
                                                                                                 self.var_nationality.get(),
                                                                                                 self.var_id_proof.get(),
                                                                                                 self.var_id_number.get(),
                                                                                                 self.var_address.get(),
                                                                                                 self.var_email.get(),
                                                                                                 ))
                connect.commit()
                self.fetch_data()
                connect.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except EXCEPTION as e:
                messagebox.showwarning("Warning", f"Something went wrong:{str(e)}", parent=self.root)

    def fetch_data(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
        cursor = connect.cursor()
        cursor.execute("select * from customer")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.customer_details_table.delete(*self.customer_details_table.get_children())
            for data in rows:
                self.customer_details_table.insert("",END, values=data)
            connect.commit()
        else:
            messagebox.showerror("Error", "No data is present in database", parent=self.root)
        connect.close()

    def get_cursor(self, events=""):
        cursor_row = self.customer_details_table.focus()
        content = self.customer_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_lname.set(row[2])
        self.var_gender.set(row[3])
        self.var_postcode.set(row[4])
        self.var_mobile.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])
        self.var_email.set(row[10])

    def update(self):
        if self.var_mobile.get() == "" or self.var_id_number.get() == "" or self.var_name.get() == "" or self.var_lname.get() == "" or self.var_gender.get() ==  ""\
                or self.var_postcode.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "" or self.var_id_proof.get() == "" \
                or self.var_address.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
            cursor = connect.cursor()
            cursor.execute("update customer set Name=%s, LastName=%s, Gender=%s, Postcode=%s, Mobile=%s, Nationality=%s, Idproof=%s, Idnumber=%s, "
                           "Address=%s, email=%s where Ref=%s",(
                                                            self.var_name.get(),
                                                            self.var_lname.get(),
                                                            self.var_gender.get(),
                                                            self.var_postcode.get(),
                                                            self.var_mobile.get(),
                                                            self.var_nationality.get(),
                                                            self.var_id_proof.get(),
                                                            self.var_id_number.get(),
                                                            self.var_address.get(),
                                                            self.var_email.get(),
                                                            self.var_ref.get()))
            connect.commit()
            self.fetch_data()
            connect.close()
            messagebox.showinfo("Update", "Customer details has been successfully updated", parent=self.root)

    def delete(self):
        yesno = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer detail", parent=self.root)
        if yesno > 0:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
            cursor = connect.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            cursor.execute(query, value)
            connect.commit()
            self.fetch_data()
            connect.close()
        else:
            if not yesno:
                return

    def reset(self):
        # self.var_ref.set("")
        self.var_name.set("")
        self.var_lname.set("")
        # self.var_gender.set("")
        self.var_postcode.set("")
        self.var_mobile.set("")
        # self.var_nationality.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        self.var_email.set("")
        x = random.randrange(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767", database="management")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM customer WHERE Ref=" + str(self.entry_var.get()))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.customer_details_table.delete(*self.customer_details_table.get_children())
            for i in rows:
                self.customer_details_table.insert("", END, values=i)
            connect.commit()
        connect.close()


if __name__ == "__main__":
    root = Tk()
    obj = Customer(root)
    root.mainloop()
