from tkinter import *
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass@123",
    database="patient_ms_db"
)
myc= db.cursor()

w = Tk()
w.geometry("1300x720")
w.config(background="#c5fae8")

def mySearch():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Patient Appointments")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                        text="Hospital",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                        text="Employee",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                        text="Medicine",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                        text="Appointment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                        text="Reports",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                        text="Insurance",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                        text="Payment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                        text="Wards",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l2 = Label(w,
               text="Patient ID:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l2.place(x=100, y=175)

    e1 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e1.place(x=300, y=175)

    search_results_text = Text(w, wrap='word',height=15,width=90,bg="#f4f5ba",fg="#45856f",font=("Baskerville Old Face",15))
    search_results_text.place(x=200, y=250)


    # Scrollbar for the text widget
    scrollbar = Scrollbar(w, command=search_results_text.yview)
    scrollbar.place(x=1350, y=150, relheight=0.4)
    search_results_text.config(yscrollcommand=scrollbar.set)

    def search_patients():
        search_results_text.delete(1.0, 'end')  # Clear previous results

        #Searching from patients table.
        q1=f"SELECT p_name FROM patients where p_id={e1.get()}"
        myc.execute(q1)
        r1=myc.fetchall()
        for p_name in r1:
            search_results_text.insert('end', f"Patient details:\nPatient's name:{p_name}\n")

        # Searching from hospital table.
        q2 = f"SELECT h_regno,h_name FROM hospital h,patients p where h.p_id=p.p_id and p.p_id={e1.get()}"
        myc.execute(q2)
        r2 = myc.fetchall()
        for h_reg, h_name in r2:
            search_results_text.insert('end',f"\nHospital details:\nHospital Reg no.: {h_reg}\nHospital name: {h_name}\n")

        # Searching from doctor table.
        q3= f"SELECT e_name,specialization FROM patients p,employees e, doctor d WHERE d.p_id=p.p_id and e.e_id=d.e_id and p.p_id={e1.get()}"
        myc.execute(q3)
        r3 = myc.fetchall()
        for e_name,spec in r3:
            search_results_text.insert('end', f"\nDoctor details:\nDoctor's name:{e_name}\nSpecialization:{spec}\n")

        # Searching from medicines table.
        q4 = f"SELECT m_name,m_dosage FROM patients p, medicine m WHERE m.p_id=p.p_id and p.p_id={e1.get()}"
        myc.execute(q4)
        r4 = myc.fetchall()
        for m_name,m_dosage in r4:
            search_results_text.insert('end', f"\nMedicine details:\nMedicine name:{m_name}\nDosage:{m_dosage}\n")

        # Searching from ward table.
        q5 = f"SELECT w_no,w_type,w_location FROM patients p, ward w WHERE w.p_id=p.p_id and p.p_id={e1.get()}"
        myc.execute(q5)
        r5 = myc.fetchall()
        for w_no,w_type,w_loc in r5:
            search_results_text.insert('end', f"\nWard details:\nWard no.:{w_no}\nWard type:{w_type}\nWard location:{w_loc}\n")

        # Searching from report table.
        q6 = f"SELECT r_no,r_type,r_date FROM patients p, reports r WHERE r.p_id=r.p_id and p.p_id={e1.get()}"
        myc.execute(q6)
        r6 = myc.fetchall()
        for r_no, r_type, r_date in r6:
            search_results_text.insert('end',f"\nReport details:\nReport no.:{r_no}\nReport type:{r_type}\nReport date:{r_date}\n")

        # Searching from insurance table.
        q7 = f"SELECT p_no,company,p_type,amt FROM patients p, insurance i WHERE i.p_id=p.p_id and p.p_id={e1.get()}"
        myc.execute(q7)
        r7 = myc.fetchall()
        for p_no, company, p_type,amt in r7:
            search_results_text.insert('end',f"\nInsurance details:\nPolicy no.:{p_no}\nInsurance Company:{company}\nPolicy type:{p_type}\nAmount:{amt}\n")

        # Searching from payment table.
        q8= f"SELECT recipt_no,p_methods,p_amt FROM patients p, payments py WHERE py.p_id=p.p_id and p.p_id={e1.get()}"
        myc.execute(q8)
        r8 = myc.fetchall()
        for recipt_no,p_method,amt in r8:
            search_results_text.insert('end',f"\nPayment details:\nReceipt no.:{recipt_no}\nPayment method:{p_method}\nAmount:{amt}\n")

    b12 = Button(w,
                 text="Search",
                 font=("Baskerville Old Face", 25),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=search_patients)
    b12.place(x=550, y=620)

    w.mainloop()

def Patients():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Patient Appointments")


    f = Frame(w)
    f.pack()

    b1 = Button(f,
                        text="Patient",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=lambda: (Patients()))
    b1.pack(side=LEFT)

    b2 = Button(f,
                        text="Hospital",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=lambda :(Hospital(),w.destroy()))
    b2.pack(side=LEFT)

    b3 = Button(f,
                        text="Employee",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                        text="Medicine",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                        text="Appointment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                        text="Reports",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                        text="Insurance",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                        text="Payment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                        text="Wards",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11= Button(f,
                text="Search",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Patient Appointments",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
                    text="Patient ID:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l2.place(x=100, y=175)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=300, y=175)

    l3 = Label(w,
                    text="Patient Name:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l3.place(x=100, y=250)

    e2 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e2.place(x=300, y=250)

    l4 = Label(w,
                    text="Patient Age:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l4.place(x=100, y=325)

    e3 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e3.place(x=300, y=325)

    l5 = Label(w,
                    text="Patient Address:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l5.place(x=100, y=400)

    e4 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e4.place(x=325, y=400)

    def add_patient():
        p_id = e1.get()
        p_name = e2.get()
        p_age = e3.get()
        p_address = e4.get()

        query="insert into patients (p_id,p_name,p_age,p_address) values (%s,%s,%s,%s)"
        val=(p_id,p_name,p_age,p_address)
        myc.execute(query,val)
        db.commit()

    b10 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_patient)
    b10.place(x=480, y=500)

    w.mainloop()

def Hospital():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Hospital")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                text="Hospital",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                text="Employee",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                text="Medicine",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                text="Appointment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                text="Reports",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                text="Insurance",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                text="Payment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                text="Wards",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                text="Hospital Details",
                bg="#c5fae8",
                font=("Times New Roman", 30, "underline"),
                fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
                text="Hospital Registration No.:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l2.place(x=150, y=175)

    e1 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e1.place(x=500, y=175)

    l3 = Label(w,
                text="Hospital Name:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l3.place(x=150, y=250)

    e2 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e2.place(x=500, y=250)

    l4 = Label(w,
                text="Hospital Address:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l4.place(x=150, y=335)

    e3 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e3.place(x=500, y=335)

    l5 = Label(w,
                text="Hospital Contact:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l5.place(x=150, y=425)

    e4 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e4.place(x=500, y=425)

    l6 = Label(w,
                text="Hospital Type:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l6.place(x=150, y=500)

    e5 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e5.place(x=500, y=500)

    l = Label(w,
               text="Patient ID:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l.place(x=800, y=175)

    e=Entry(w,
            font=("Baskerville Old Face", 20),
            bg="#f4f5ba",
            fg="#45856f")
    e.place(x=1000, y=175)

    def add_hospital():
        h_regno = e1.get()
        h_name = e2.get()
        h_address = e3.get()
        h_contact = e4.get()
        h_type = e5.get()
        p_id=e.get()

        query = "insert into hospital (h_regno,h_name,h_address,h_contact,h_type,p_id) values (%s,%s,%s,%s,%s,%s)"
        val = (h_regno,h_name,h_address,h_contact,h_type,p_id)
        myc.execute(query, val)
        db.commit()

    b3 = Button(w,
                text="Submit",
                font=("Baskerville Old Face", 25),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=add_hospital)
    b3.place(x=580, y=600)

    w.mainloop()

def Employee():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Employee Details")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                        text="Patient",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                        text="Hospital",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0")
    b2.pack(side=LEFT)

    b3 = Button(f,
                        text="Employee",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                        text="Medicine",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                        text="Appointment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                        text="Reports",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                        text="Insurance",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                        text="Payment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                        text="Wards",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Employee Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=100, y=90)

    l2 = Label(w,
                    text="Employee ID:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l2.place(x=100, y=150)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=400, y=150)

    l3 = Label(w,
                    text="Employee Name:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l3.place(x=100, y=200)

    e2 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e2.place(x=400, y=200)

    l4 = Label(w,
                    text="Employee Age:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l4.place(x=100, y=250)

    e3 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e3.place(x=400, y=250)

    # Doctor Sub-entity
    l7 = Label(w,
                    text="Doctor Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l7.place(x=100,y=350)

    l5 = Label(w,
                    text="Specialization:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l5.place(x=100, y=400)

    e4 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e4.place(x=400, y=400)

    # Nurse Sub-entity
    l8 = Label(w,
                    text="Nurse Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l8.place(x=100, y=475)

    l6 = Label(w,
                    text="Qualifications:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l6.place(x=100, y=525)

    e5 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e5.place(x=400, y=525)

    l = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l.place(x=800, y=150)

    e = Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e.place(x=1000, y=150)

    def add_employee():
        e_id = e1.get()
        e_name = e2.get()
        e_age = e3.get()
        p_id=e.get()

        query = "insert into employees (e_id,e_name,e_age,p_id) values (%s,%s,%s,%s)"
        val = (e_id,e_name,e_age,p_id)
        myc.execute(query, val)
        db.commit()

        # Doctor Sub-entity
        specialization = e4.get()
        query = "insert into doctor (e_id,specialization,p_id) values (%s,%s,%s)"
        val = (e_id,specialization,p_id)
        myc.execute(query, val)
        db.commit()

        # Nurse Sub-entity
        qualifications = e5.get()
        query = "insert into nurse (e_id,qualifications,p_id) values (%s,%s,%s)"
        val = (e_id,qualifications,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_employee)
    b10.place(x=580, y=600)

    w.mainloop()

def Medicine():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Medicine Details")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                        text="Patient",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                        text="Hospital",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                        text="Employee",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                        text="Medicine",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                        text="Appointment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                        text="Reports",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                        text="Insurance",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                        text="Payment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                        text="Wards",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Medicine Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=60, y=100)

    l2 = Label(w,
                    text="Medicine Code:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l2.place(x=60, y=175)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=300, y=175)

    l3 = Label(w,
                    text="Medicine Name:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l3.place(x=60, y=250)

    e2 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e2.place(x=300, y=250)

    l4 = Label(w,
                    text="Dosage:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l4.place(x=60, y=325)

    e3 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e3.place(x=300, y=325)

    l5 = Label(w,
                    text="Medicine Type:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l5.place(x=60, y=400)

    e4 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e4.place(x=300, y=400)

    l6 = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l6.place(x=60, y=475)

    e5= Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e5.place(x=300, y=475)

    def add_medicine():
        m_code = e1.get()
        m_name = e2.get()
        m_dosage = e3.get()
        m_type = e4.get()
        p_id=e5.get()

        query = "insert into medicine (m_code,m_name,m_dosage,m_type,p_id) values (%s,%s,%s,%s,%s)"
        val = (m_code,m_name,m_dosage,m_type,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_medicine)
    b10.place(x=200, y=600)

    l7 = Label(w,
               text="Modify Medicine Details",
               bg="#c5fae8",
               font=("Times New Roman", 30, "underline"),
               fg="#45856f")
    l7.place(x=650, y=100)

    l8 = Label(w,
               text="Old Medicine name:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l8.place(x=700, y=175)

    e6 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e6.place(x=1000, y=175)

    l9 = Label(w,
               text="New Medicine name:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l9.place(x=700, y=250)

    e7 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e7.place(x=1000, y=250)

    l10 = Label(w,
               text="Old Dosage:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l10.place(x=700, y=325)

    e8= Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e8.place(x=1000, y=325)

    l11=Label(w,
               text="New Dosage:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l11.place(x=700, y=400)

    e9= Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e9.place(x=1000, y=400)

    l12= Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l12.place(x=700, y=475)

    e10= Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e10.place(x=1000, y=475)

    def modify_medicine():
        old_m_name = e6.get()
        new_m_name = e7.get()
        old_m_dosage = e8.get()
        new_m_dosage = e9.get()
        p_id = e10.get()

        query = f"UPDATE medicine SET m_name = '{new_m_name}', m_dosage = '{new_m_dosage}' WHERE p_id='{p_id}' and m_name='{old_m_name}' and m_dosage='{old_m_dosage}'"
        myc.execute(query)
        db.commit()

    b12= Button(w,
                 text="Modify",
                 font=("Baskerville Old Face", 35),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=modify_medicine)
    b12.place(x=800, y=600)

    w.mainloop()

def Appointments():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Appointments")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                        text="Patient",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                        text="Hospital",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                        text="Employee",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                        text="Medicine",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                        text="Appointment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                        text="Reports",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                        text="Insurance",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                        text="Payment",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                        text="Wards",
                        font=("Baskerville Old Face", 20),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Appointments",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=100, y=90)

    l2 = Label(w,
                    text="Appointment No.:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l2.place(x=100, y=200)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 25),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=400, y=200)

    l3 = Label(w,
                    text="Appointment Type:",
                    bg="#c5fae8",
                    font=("Times New Roman", 30),
                    fg="#45856f")
    l3.place(x=100, y=300)

    a_type = ["Online", "Offline"]
    x = IntVar()

    for i in range(len(a_type)):
        rb = Radiobutton(w,
                            text=a_type[i],
                            font=("Baskerville Old Face", 20),
                            variable=x,
                            value=i,
                            bg="#c5fae8",
                            fg="#45856f",
                            activebackground="#c5fae8",
                            activeforeground="#45856f",
                            padx=25)
        rb.place(x=430 + i * 200, y=300)

        l4 = Label(w,
                        text="Timing:",
                        bg="#c5fae8",
                        font=("Times New Roman", 30),
                        fg="#45856f")
        l4.place(x=100, y=400)

        e2 = Entry(w,
                        font=("Baskerville Old Face", 25),
                        bg="#f4f5ba",
                        fg="#45856f")
        e2.place(x=250, y=400)

        l = Label(w,
                  text="Patient ID:",
                  bg="#c5fae8",
                  font=("Times New Roman", 25),
                  fg="#45856f")
        l.place(x=800, y=200)

        e = Entry(w,
                  font=("Baskerville Old Face", 20),
                  bg="#f4f5ba",
                  fg="#45856f")
        e.place(x=1000, y=200)

    def add_appointment():
        a_no = e1.get()
        a_type = "Online" if x.get() == 0 else "Offline"
        a_timing = (e2.get())
        p_id=e.get()

        query = "insert into appointments (a_no,a_type,a_timing,p_id) values (%s,%s,%s,%s)"
        val = (a_no,a_type,a_timing,p_id)
        myc.execute(query, val)
        db.commit()



    b3 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_appointment)
    b3.place(x=580, y=600)

    w.mainloop()

def Reports():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Reports")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                text="Hospital",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                text="Employee",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                text="Medicine",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                text="Appointment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                text="Reports",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                text="Insurance",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                text="Payment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                text="Wards",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                text="Report Details",
                bg="#c5fae8",
                font=("Times New Roman", 30, "underline"),
                fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
                text="Report No.:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l2.place(x=150, y=175)

    e1 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e1.place(x=400, y=175)

    l3 = Label(w,
                text="Report Type:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l3.place(x=150, y=250)

    e2 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e2.place(x=400, y=250)

    l4 = Label(w,
                text="Report Date:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l4.place(x=150, y=325)

    e3 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e3.place(x=400, y=325)

    l5 = Label(w,
                text="Number of Reports:",
                bg="#c5fae8",
                font=("Times New Roman", 25),
                fg="#45856f")
    l5.place(x=150, y=400)

    e4 = Entry(w,
                font=("Baskerville Old Face", 20),
                bg="#f4f5ba",
                fg="#45856f")
    e4.place(x=430, y=400)

    l = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l.place(x=800, y=175)

    e = Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e.place(x=1000, y=175)

    def add_report():
        report_no = e1.get()
        report_type = e2.get()
        report_date = e3.get()
        no_of_reports = e4.get()
        p_id=e.get()

        query = "insert into reports (r_no,r_type,r_date,no_of_reports,p_id) values (%s,%s,%s,%s,%s)"
        val = (report_no,report_type,report_date,no_of_reports,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                  text="Submit",
                  font=("Baskerville Old Face", 35),
                  bg="#82baa0",
                  fg="#c5fae8",
                  activeforeground="#c5fae8",
                  activebackground="#82baa0",
                  command=add_report)
    b10.place(x=580, y=500)

    w.mainloop()

def Ward():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Wards")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                text="Hospital",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                text="Employee",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                text="Medicine",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                text="Appointment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                text="Reports",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                text="Insurance",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                text="Payment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                text="Wards",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Ward Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
                    text="Ward No.:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l2.place(x=150, y=175)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=400, y=175)

    l3 = Label(w,
                    text="Ward Type:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l3.place(x=150, y=250)

    e2 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e2.place(x=400, y=250)

    l4 = Label(w,
                    text="Ward Location:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l4.place(x=150, y=325)

    e3 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e3.place(x=400, y=325)

    l = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l.place(x=800, y=175)

    e = Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e.place(x=1000, y=175)

    def add_ward():
        ward_no = e1.get()
        ward_type = e2.get()
        ward_location = e3.get()
        p_id=e.get()

        query = "insert into ward (w_no,w_type,w_location,p_id) values (%s,%s,%s,%s)"
        val = (ward_no,ward_type,ward_location,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_ward)
    b10.place(x=580, y=400)

    w.mainloop()

def Payments():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Payments")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                text="Hospital",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                text="Employee",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                text="Medicine",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                text="Appointment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                text="Reports",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                text="Insurance",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                text="Payment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                text="Wards",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
               text="Payment Details",
               bg="#c5fae8",
               font=("Times New Roman", 30, "underline"),
               fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
               text="Receipt No.:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l2.place(x=150, y=175)

    e1 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e1.place(x=400, y=175)

    l3 = Label(w,
               text="Payment Method:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l3.place(x=150, y=250)

    e2 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e2.place(x=400, y=250)

    l4 = Label(w,
               text="Payment Amount:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l4.place(x=150, y=325)

    e3 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e3.place(x=400, y=325)

    l5 = Label(w,
               text="Installments:",
               bg="#c5fae8",
               font=("Times New Roman", 25),
               fg="#45856f")
    l5.place(x=150, y=400)

    e4 = Entry(w,
               font=("Baskerville Old Face", 20),
               bg="#f4f5ba",
               fg="#45856f")
    e4.place(x=400, y=400)

    l = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l.place(x=800, y=175)

    e = Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e.place(x=1000, y=175)

    def add_payment():
        receipt_no = e1.get()
        payment_method = e2.get()
        payment_amount = e3.get()
        installments = e4.get()
        p_id=e.get()

        query = "insert into payments (recipt_no,p_methods,p_amt,installments,p_id) values (%s,%s,%s,%s,%s)"
        val = (receipt_no,payment_method,payment_amount,installments,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                 text="Submit",
                 font=("Baskerville Old Face", 35),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=add_payment)
    b10.place(x=580, y=500)
    w.mainloop()

def Insurance():
    for widget in w.winfo_children():
        widget.destroy()
    w.title("Insurance Details")

    f = Frame(w)
    f.pack()

    b1 = Button(f,
                text="Patient",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Patients)
    b1.pack(side=LEFT)

    b2 = Button(f,
                text="Hospital",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Hospital)
    b2.pack(side=LEFT)

    b3 = Button(f,
                text="Employee",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Employee)
    b3.pack(side=LEFT)

    b4 = Button(f,
                text="Medicine",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Medicine)
    b4.pack(side=LEFT)

    b5 = Button(f,
                text="Appointment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Appointments)
    b5.pack(side=LEFT)

    b6 = Button(f,
                text="Reports",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Reports)
    b6.pack(side=LEFT)

    b7 = Button(f,
                text="Insurance",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Insurance)
    b7.pack(side=LEFT)

    b8 = Button(f,
                text="Payment",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Payments)
    b8.pack(side=LEFT)

    b9 = Button(f,
                text="Wards",
                font=("Baskerville Old Face", 20),
                bg="#82baa0",
                fg="#c5fae8",
                activeforeground="#c5fae8",
                activebackground="#82baa0",
                command=Ward)
    b9.pack(side=LEFT)

    b11 = Button(f,
                 text="Search",
                 font=("Baskerville Old Face", 20),
                 bg="#82baa0",
                 fg="#c5fae8",
                 activeforeground="#c5fae8",
                 activebackground="#82baa0",
                 command=mySearch)
    b11.pack(side=LEFT)

    l1 = Label(w,
                    text="Insurance Details",
                    bg="#c5fae8",
                    font=("Times New Roman", 30, "underline"),
                    fg="#45856f")
    l1.place(x=100, y=100)

    l2 = Label(w,
                    text="Policy Number:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l2.place(x=100, y=175)

    e1 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e1.place(x=400, y=175)

    l3 = Label(w,
                    text="Policy Type:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l3.place(x=100, y=250)

    e2 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e2.place(x=400, y=250)

    l4 = Label(w,
                    text="Amount:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l4.place(x=100, y=325)

    e3 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e3.place(x=400, y=325)

    l5 = Label(w,
                    text="Coverage:",
                    bg="#c5fae8",
                    font=("Times New Roman", 25),
                    fg="#45856f")
    l5.place(x=100, y=400)

    e4 = Entry(w,
                    font=("Baskerville Old Face", 20),
                    bg="#f4f5ba",
                    fg="#45856f")
    e4.place(x=400, y=400)

    l = Label(w,
              text="Patient ID:",
              bg="#c5fae8",
              font=("Times New Roman", 25),
              fg="#45856f")
    l.place(x=800, y=175)

    e = Entry(w,
              font=("Baskerville Old Face", 20),
              bg="#f4f5ba",
              fg="#45856f")
    e.place(x=1000, y=175)

    def add_insurance():
        p_no = e1.get()
        p_type = e2.get()
        amt = e3.get()
        company = e4.get()
        p_id=e.get()

        query = "insert into insurance (p_no,p_type,amt,company,p_id) values (%s,%s,%s,%s,%s)"
        val = (p_no,p_type,amt,company,p_id)
        myc.execute(query, val)
        db.commit()

    b10 = Button(w,
                        text="Submit",
                        font=("Baskerville Old Face", 35),
                        bg="#82baa0",
                        fg="#c5fae8",
                        activeforeground="#c5fae8",
                        activebackground="#82baa0",
                        command=add_insurance)
    b10.place(x=580, y=500)

    w.mainloop()

Patients()