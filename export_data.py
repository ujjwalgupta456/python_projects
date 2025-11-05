import sqlite3
import pandas as pd
conn = sqlite3.connect("student.db")
df = pd.read_sql_query("SELECT * FROM enrollments",conn)
df.to_csv("enrolled students.csv",index=False)
conn.close()