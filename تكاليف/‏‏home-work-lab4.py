# إعداد قاعدة البيانات 
import sqlite3 as sql
con=sql.connect("D:\الجامعه\مستوى ثالث\الترم الثاني\برمجة متقدمة\تكاليف\medical_center.db")
cursor=con.cursor()

# إنشاء الجداول
def create_table():
#     جدول المرضى
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        patient_id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT
    )
    """)
# جدول الاطباء
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors (
        doctor_id INTEGER PRIMARY KEY,
        name TEXT,
        specialization TEXT
    )
    """)
# جدول الزيارات
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Visits (
        visit_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        visit_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
    )
    """)
# جدول التحاليل
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tests (
        test_id INTEGER PRIMARY KEY,
        test_name TEXT,
        cost REAL
    )
    """)
# جدول تحاليل المرضى
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patient_Tests (
        pt_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        test_id INTEGER,
        doctor_id INTEGER,
        test_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (test_id) REFERENCES Tests(test_id),
        FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
    )
    """)
# جدول الغرف
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Rooms (
        room_id INTEGER PRIMARY KEY,
        room_number INTEGER
    )
    """)
# جدول الرقود
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Admissions (
        admission_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        room_id INTEGER,
        entry_date TEXT,
        exit_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
    )
    """)

    con.commit()
create_table()

# المرضى الذين زاروا طبيبًا معينًا
def patients_visited_doctor(doctor_id):
    cursor.execute("""
    SELECT DISTINCT Patients.name FROM Patients 
    JOIN Visits ON Patients.patient_id = Visits.patient_id 
    WHERE Visits.doctor_id = ? """, (doctor_id,))
    return cursor.fetchall()
patients_visited_doctor(7)

# حساب تكلفة التحاليل لمريض معين
def total_tests_cost(patient_id):
    cursor.execute(""" SELECT SUM(Tests.cost) FROM Tests
    JOIN Patient_Tests ON Tests.test_id = Patient_Tests.test_id
    WHERE Patient_Tests.patient_id = ? """, (patient_id,))
    return cursor.fetchone()[0]
total_tests_cost(12)

# الغرف التي أقيم فيها المرضى بتاريخ معين
def rooms_on_date(date):
    cursor.execute(""" SELECT DISTINCT Rooms.room_number FROM Rooms
    JOIN Admissions ON Rooms.room_id = Admissions.room_id 
    WHERE ? BETWEEN entry_date AND exit_date """, (date,))
    return cursor.fetchall()

# تواريخ الزيارات والتحاليل لمريض معين
def visits_and_tests_dates(patient_id):
    cursor.execute(""" SELECT visit_date FROM Visits
    WHERE patient_id = ? UNION SELECT test_date FROM Patient_Tests
    WHERE patient_id = ? """, (patient_id, patient_id))
    return cursor.fetchall()

# الأطباء الذين أشرفوا على تحليل في تخصص معين
def doctors_by_specialization(specialization):
    cursor.execute(""" SELECT DISTINCT Doctors.name FROM Doctors 
    JOIN Patient_Tests ON Doctors.doctor_id = Patient_Tests.doctor_id 
    WHERE Doctors.specialization = ? """, (specialization,)) 
    return cursor.fetchall()


# المرضى الذين أجروا أكثر من تحليل
def patients_more_than_one_test():
    cursor.execute(""" SELECT Patients.name FROM Patients
    JOIN Patient_Tests ON Patients.patient_id = Patient_Tests.patient_id
    GROUP BY Patients.patient_id HAVING COUNT(Patient_Tests.test_id) > 1 """) 
    return cursor.fetchall() 

# الأطباء الذين لم يشرفوا على أي تحليل
def doctors_without_tests():
    cursor.execute(""" SELECT Doctors.name FROM Doctors
    LEFT JOIN Patient_Tests ON Doctors.doctor_id = Patient_Tests.doctor_id 
    WHERE Patient_Tests.test_id IS NULL """)
    return cursor.fetchall()

# المرضى الذين أقاموا أكثر من 7 أيام
def patients_more_than_7_days():
    cursor.execute(""" SELECT Patients.name FROM Patients 
    JOIN Admissions ON Patients.patient_id = Admissions.patient_id
    WHERE julianday(exit_date) - julianday(entry_date) > 7 """)
    return cursor.fetchall()


# التحاليل التي تكلفتها أكثر من 500
def expensive_tests():
    cursor.execute(""" SELECT * FROM Tests WHERE cost > 500 """)
    return cursor.fetchall()

# تفاصيل زيارات مريض معين
def patient_visits(patient_id):
    cursor.execute(""" SELECT * FROM Visits
    WHERE patient_id = ? """, (patient_id,))
    return cursor.fetchall()

# اغلاق الاتصال
con.close()
