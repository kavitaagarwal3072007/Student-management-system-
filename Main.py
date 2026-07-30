import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_student():
    print("\n--- NEW STUDENT ADD KAREN ---")
    name = input("Student Name: ").strip()
    roll_no = input("Roll Number: ").strip()
    course = input("Course Name: ").strip()

    if not name or not roll_no or not course:
        print("\n❌ Sabhi fields bharna zaroori hai!\n")
        return

    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, roll_no, course) VALUES (?, ?, ?)", 
                       (name, roll_no, course))
        conn.commit()
        print("\n✅ Student successfully add ho gaya!\n")
    except sqlite3.IntegrityError:
        print("\n❌ Yeh Roll Number pehle se exist karta hai!\n")
    finally:
        conn.close()

def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("\n⚠️ KOI STUDENT RECORD NAHI MILA.\n")
        return

    print("\n" + "="*50)
    print(f"{'ID':<5} | {'Name':<15} | {'Roll No':<10} | {'Course':<10}")
    print("="*50)
    for row in records:
        print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<10} | {row[3]:<10}")
    print("="*50 + "\n")

def delete_student():
    roll_no = input("\nJis student ko delete karna hai uska Roll No likhein: ").strip()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    
    if cursor.rowcount > 0:
        print("\n✅ Student record delete ho gaya!\n")
    else:
        print("\n❌ Yeh Roll Number nahi mila.\n")
    
    conn.commit()
    conn.close()

def main_menu():
    init_db()
    while True:
        print("=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit System")
        
        choice = input("\nOption chuniye (1-4): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("\nDhanyawad! System band ho raha hai...\n")
            break
        else:
            print("\n❌ Galat option! Kripya 1 se 4 ke beech chunein.\n")

if __name__ == "__main__":
    main_menu()
