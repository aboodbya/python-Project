import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ================= Database =================
conn = sqlite3.connect("D:\الجامعه\مستوى ثالث\الترم الثاني\برمجة متقدمة\تكاليف\employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job TEXT,
    gender TEXT,
    age INTEGER,
    email TEXT,
    mobile TEXT,
    address TEXT
)
""")
conn.commit()

# ================= Main Window =================
root = tk.Tk()
root.title("Employee Management")
root.state("zoomed")
root.resizable(False, False)

# ================= Variables =================
name_var = tk.StringVar()
job_var = tk.StringVar()
gender_var = tk.StringVar()
age_var = tk.StringVar()
email_var = tk.StringVar()
mobile_var = tk.StringVar()

# ================= Functions =================
def clear():
    name_var.set("")
    job_var.set("")
    gender_var.set("")
    age_var.set("")
    email_var.set("")
    mobile_var.set("")
    address_text.delete("1.0", tk.END)

def display():
    tv.delete(*tv.get_children())
    cursor.execute("SELECT * FROM employee")
    for row in cursor.fetchall():
        tv.insert("", tk.END, values=row)

def insert():
    if name_var.get() == "" or job_var.get() == "":
        messagebox.showerror("Error", "Name and Job are required")
        return

    cursor.execute(
        "INSERT INTO employee VALUES (NULL,?,?,?,?,?,?,?)",
        (
            name_var.get(),
            job_var.get(),
            gender_var.get(),
            age_var.get(),
            email_var.get(),
            mobile_var.get(),
            address_text.get("1.0", tk.END)
        )
    )
    conn.commit()
    display()
    clear()

def get_data(event):
    selected = tv.focus()
    data = tv.item(selected)
    row = data["values"]

    if row:
        name_var.set(row[1])
        job_var.set(row[2])
        gender_var.set(row[3])
        age_var.set(row[4])
        email_var.set(row[5])
        mobile_var.set(row[6])
        address_text.delete("1.0", tk.END)
        address_text.insert(tk.END, row[7])

def update():
    selected = tv.focus()
    data = tv.item(selected)
    row = data["values"]

    if not row:
        return

    cursor.execute("""
    UPDATE employee SET
    name=?, job=?, gender=?, age=?, email=?, mobile=?, address=?
    WHERE id=?
    """, (
        name_var.get(),
        job_var.get(),
        gender_var.get(),
        age_var.get(),
        email_var.get(),
        mobile_var.get(),
        address_text.get("1.0", tk.END),
        row[0]
    ))

    conn.commit()
    display()
    clear()

def delete():
    selected = tv.focus()
    data = tv.item(selected)
    row = data["values"]

    if not row:
        return

    cursor.execute("DELETE FROM employee WHERE id=?", (row[0],))
    conn.commit()
    display()
    clear()

# ================= Left Frame =================
left = tk.Frame(root, bg="#0f172a", width=350)
left.pack(side=tk.LEFT, fill=tk.Y)

title = tk.Label(left, text="Employee Company",
                 bg="#0f172a", fg="white",
                 font=("Arial", 18, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=15)

def make_row(text, var, r):
    tk.Label(left, text=text, bg="#0f172a", fg="white",font=("Arial", 18, "bold")) \
        .grid(row=r, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(left, textvariable=var, width=25,
            font=("Arial", 18, "bold") ) \
        .grid(row=r, column=1, padx=10, pady=5)

make_row("Name", name_var, 1)
make_row("Job", job_var, 2)

tk.Label(left, text="Gender", bg="#0f172a", fg="white",font=("Arial", 18, "bold")) \
    .grid(row=3, column=0, padx=10, pady=5, sticky="w",)
ttk.Combobox(left, textvariable=gender_var,
             values=["male", "female"],
             font=("Arial", 18, "bold"),
             state="readonly", width=22) \
    .grid(row=3, column=1, padx=10, pady=5)

make_row("Age", age_var, 4)
make_row("Email", email_var, 5)
make_row("Mobile", mobile_var, 6)

tk.Label(left, text="Address", bg="#0f172a", fg="white",font=("Arial", 18, "bold")) \
    .grid(row=7, column=0, padx=10, pady=5, sticky="nw")

address_text = tk.Text(left, height=3, width=25)
address_text.grid(row=7, column=1, padx=10, pady=5)

# Buttons
tk.Button(left, text="Add Details", bg="#22c55e",
          width=18,height=4, command=insert) \
    .grid(row=8, column=0, pady=10)

tk.Button(left, text="Delete Details", bg="#ef4444",
          width=18, height=4,command=delete) \
    .grid(row=8, column=1, pady=10)

tk.Button(left, text="Update Details", bg="#3b82f6",
          width=18,height=4,command=update) \
    .grid(row=9, column=0, pady=5)

tk.Button(left, text="Clear Details", bg="#f59e0b",
          width=18,height=4, command=clear) \
    .grid(row=9, column=1, pady=5)

# ================= Right Frame =================
right = tk.Frame(root, bg="white")
right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

cols = ("ID", "Name", "Job", "Gender", "Age", "Email", "Mobile", "Address")
tv = ttk.Treeview(right, columns=cols, show="headings")

for col in cols:
    tv.heading(col, text=col)
    tv.column(col, width=100)

tv.pack(fill=tk.BOTH, expand=True)
tv.bind("<ButtonRelease-1>", get_data)

# ================= Start =================
display()
root.mainloop()
