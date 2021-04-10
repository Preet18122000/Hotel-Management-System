from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector


class RoomDetail:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+230+220")

        # variables
        self.var_floor = StringVar()
        self.var_room_no = StringVar()
        self.var_room_type = StringVar()

        # ----------------- Heading and logo ------------------------
        labeltitle = Label(self.root, text="ROOM DETAILS PANEL", font=("times new roman", 18, "bold"), bd=2, fg="white", bg="black", relief=RIDGE)
        labeltitle.place(x=5, y=0, width=1295, height=50)

        img1 = Image.open(r"C:\Users\preet\Desktop\hotel-management-system\images\hotellogo.jpg")
        img1 = img1.resize((120, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)
        labelimglogo = Label(self.root, image=self.photoimg, bd=0, relief=RIDGE)
        labelimglogo.place(x=5, y=0, width=100, height=50)

        #  ------------------Label Frame Left -----------------------------------------
        labelframeleft = LabelFrame(self.root, text="Room Details", font=("times new roman", 18, "bold"), bd=2, relief=RIDGE, padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        #  FLoor
        label_floor = Label(labelframeleft, text="Floor", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_floor.grid(row=0, column=0, sticky=W, padx=20)
        floor_entry = ttk.Entry(labelframeleft,textvariable=self.var_floor, font=("times new roman", 13, "bold"), width=29)
        floor_entry.grid(row=0, column=1)

        # Room Number
        label_room_no = Label(labelframeleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_room_no.grid(row=1, column=0, sticky=W, padx=20)
        floor_room_no = ttk.Entry(labelframeleft,textvariable=self.var_room_no, font=("times new roman", 13, "bold"), width=29)
        floor_room_no.grid(row=1, column=1)

        # Room Type
        label_roomtype = Label(labelframeleft, text="Floor Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomtype.grid(row=2, column=0, sticky=W, padx=20)
        floor_roomtype = ttk.Entry(labelframeleft, textvariable=self.var_room_type, font=("times new roman", 13, "bold"), width=29)
        floor_roomtype.grid(row=2, column=1)

        buttonframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        buttonframe.place(x=0, y=180, width=417, height=37)

        addbtn = Button(buttonframe, text="SAVE",command=self.add, font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        addbtn.grid(row=0, column=0, padx=2)

        deletebtn = Button(buttonframe, text="DELETE",command=self.delete,  font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        deletebtn.grid(row=0, column=2, padx=2)

        updatebtn = Button(buttonframe, text="UPDATE",command=self.update,  font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        updatebtn.grid(row=0, column=1, padx=2)

        resetbtn = Button(buttonframe, text="RESET",command=self.reset,  font=("times new roman", 12, "bold"), bg="black", fg="white", width=10)
        resetbtn.grid(row=0, column=3, padx=2)

    # -------------------------- search system ---------------------------
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=600, y=55, width=600, height=345)

        xscroll = Scrollbar(tableframe, orient=HORIZONTAL)
        yscroll = Scrollbar(tableframe, orient=VERTICAL)
        self.roomtable = ttk.Treeview(tableframe, column=("floor", "roomno", "roomtype"),
                                             xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.roomtable.xview)
        yscroll.config(command=self.roomtable.yview)

        self.roomtable.heading("floor", text="FLoor")
        self.roomtable.heading("roomno", text="Room No")
        self.roomtable.heading("roomtype", text="roomtype")

        self.roomtable["show"] = "headings"

        self.roomtable.column("floor", width=100)
        self.roomtable.column("roomno", width=100)
        self.roomtable.column("roomtype", width=100)

        self.roomtable.pack(fill=BOTH, expand=1)
        self.roomtable.bind("<ButtonRelease-1>", self.get_cursor)
        self.data_display()

    def add(self):
        if self.var_floor.get() == "" or  self.var_room_no.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                                  database="management")
                cursor = connect.cursor()
                cursor.execute("insert into rdetails values(%s, %s, %s)", (
                    self.var_floor.get(),
                    self.var_room_no.get(),
                    self.var_room_type.get()
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
        cursor.execute("select * from rdetails")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert("", END, values=i)
            connect.commit()
        connect.close()

    def get_cursor(self, events=""):
        cursor_data = self.roomtable.focus()
        content = self.roomtable.item(cursor_data)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])

    def update(self):
        if self.var_floor.get() == "" or  self.var_room_no.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            connect = mysql.connector.connect(host="localhost", username="root", password="p9930083767",
                                              database="management")
            cursor = connect.cursor()
            cursor.execute("update rdetails set floor=%s, roomtype=%s where roomno=%s", (
                self.var_floor.get(),
                self.var_room_type.get(),
                self.var_room_no.get(),
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
            query = "delete from rdetails where roomno=%s"
            value = (self.var_room_no.get(),)
            cursor.execute(query, value)
            connect.commit()
            self.data_display()
            connect.close()
        else:
            if not yesno:
                return

    def reset(self):
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")


if __name__=="__main__":
    root = Tk()
    obj = RoomDetail(root)
    root.mainloop()
