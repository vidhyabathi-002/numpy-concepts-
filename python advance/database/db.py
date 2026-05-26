import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    marks REAL
)
""")

print("Student table created successfully!")


conn.commit()
cursor.close()
conn.close()