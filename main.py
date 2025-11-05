import streamlit as st
import sqlite3

# page
st.set_page_config(page_title="SP Coaching Classes", page_icon="🏫", layout="wide")

#color
AQUA = "#800000"
GOLD = "#FFD700"
BG_COLOR = "#FFF8F0"

#Title of classes
st.title("🏫 SP Coaching Classes")
st.subheader("Learn, Grow, and Succeed with Us")

#navigation
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Courses Offered", "Institute Details", "Student Enrollment","ADMIN"]
)

#database
conn = sqlite3.connect('student.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS enrollments(
        name TEXT,
        age INTEGER,
        course TEXT,
        contact TEXT,
        email TEXT,
        address TEXT
    )
''')
conn.commit()


# HOME PAGE
if menu == "Home":
    st.write("""
    Welcome to **SP Coaching Classes**, your trusted learning partner for 
    students from class 6th to 12th and competitive exams like NEET and JEE.
    """)

    st.image(
        "C:\\Users\\UJJWAL\\Desktop\\python\\spclasses.jpeg",
        caption="SP Coaching Classes",
        use_container_width=True
    )

    # Achievements
    st.markdown("### 🏆 Our Achievements")
    col1, col2, col3 = st.columns(3)
    col1.metric("Students Enrolled", "500+")
    col2.metric("Board Toppers", "150+")
    col3.metric("NEET/JEE Selections", "100+")

    # Founder Message
    st.markdown("### 👨‍🏫 Message from Our Founder")
    st.info("""
    > "At SP Coaching Classes, our mission is to create an environment where every student
    > discovers their potential and achieves excellence. Education is not just about marks;
    > it's about building confidence and curiosity."
    >
    > — *Mr. P. Sharma (Founder & Director)*
    """)

    # Announcements
    st.markdown("### 📅 Announcements & Updates")
    st.success("🔔 *New Batch for Class 10th & 12th Board Students starting from 15th November!*")
    st.warning("📢 *Admissions open for NEET & JEE 2027 — Limited seats available!*")

    # Testimonials
    st.markdown("### 💬 What Our Students Say")
    st.write("⭐️ *“SP Classes helped me score 95% in my 10th Boards!”* — Riya Singh")
    st.write("⭐️ *“The doubt-solving sessions are amazing. Highly recommend!”* — Arjun Patel")


# COURSES PAGE
elif menu == "Courses Offered":
    st.header("📚 Courses Offered")
    st.write("""
    We provide coaching for:
    - Class 6th to 10th (All Subjects)
    - Class 11th & 12th (Science / Commerce / Arts)
    - NEET / JEE Preparation
    """)
    st.info("✨ Special Batch for 10th & 12th Board Students starting soon!")

# INSTITUTE DETAILS
elif menu == "Institute Details":
    st.header("🏠 Institute Details")
    st.write("""
    **Institute Name:** SP Coaching Classes  
    **Address:** Near Gaushala Ashram, Bhoidapada, Rajawali Road, Madhuban, Evershine City, Vasai(E) - 40208  
    **Contact:** +91 12345 67891  
    **Email:** spclasses191@gmail.com  
    **Head:** Mr. P. Sharma (Founder & Director)
    """)

    st.header("🕒 Timings")
    st.write("""
    **Morning Batches:**  
    - 8:00 TO 12:00 → 11th & 12th  
    - 9:00 TO 11:00 → 6th to 10th  

    **Evening Batches:**  
    - 2:00 TO 4:00 → NEET & JEE  
    - 4:00 TO 6:00 → 6th to 10th  
    - 6:00 TO 7:00 → Doubt Session
    """)

    # Faculties Section (Moved Here)
    st.header("👩‍🏫 Our Faculties")

    st.subheader("For 6th to 10th:")
    st.write("""
    - Smriti Mandhana (English)  
    - Anushka Sharma (Sanskrit)  
    - Deepti Sharma (Hindi)  
    - Jasprit Bumrah (Maths)  
    - Yashasvi Jaiswal (Social Science)  
    - Henrich Klassen (Science)  
    - Suryakumar Yadav (Geography)
    """)

    st.subheader("For 11th & 12th (Science):")
    st.write("""
    - Rohit Sharma (Physics)  
    - Virat Kohli (Maths & Statistics)  
    - Mahendra Singh (Chemistry)  
    - Jemimah Rodrigues (Biology)
    """)

    st.subheader("For 11th & 12th (Commerce):")
    st.write("""
    - Arshdeep Singh (Economics)  
    - Hardik Pandya (Book Keeping & Accountancy)  
    - Harmanpreet Kaur (Organization of Commerce & Management)  
    - Annanya Singh (Mathematics & Statistics)  
    - Shivraj Singh (Secretarial Practices)
    """)

    st.subheader("For 11th & 12th (Arts):")
    st.write("""
    - Shwetha Singh (English)  
    - Sameer Rizvi (History)  
    - Hasan Khan (Political Science)  
    - Arshdeep Singh (Economics)  
    - Khushi Chopra (Psychology)
    """)


# 🧾 STUDENT ENROLLMENT FORM
elif menu == "Student Enrollment":
    st.header("🧾 Student Enrollment Form")
    st.write("Please fill the form below to register:")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=10, max_value=22, step=1)
    course = st.selectbox("Select Course", ["Class 6th","Class 7th","class 8th","class 9th", "Class 11th", "Class 12th", "NEET", "JEE"])
    contact = st.text_input("Contact Number")
    email = st.text_input("Email ID")
    address = st.text_area("Address")

    st.info("""
    **Fees depend on standard and batch timing.**  
    **Fees must be paid within 1 week after joining.**
    """)

    if st.button("Submit"):
        if name and contact and course:
            c.execute(
                "INSERT INTO enrollments(name, age, course, contact, email, address) VALUES (?, ?, ?, ?, ?, ?)",
                (name, age, course, contact, email, address)
            )
            conn.commit()
            st.success(f"✅ Thank you {name}! You have successfully enrolled for {course}.")
            st.balloons()
        else:
            st.error("⚠️ Please fill all mandatory fields before submitting.")
elif menu == "ADMIN":
    st.header("ADMIN DASHBOARD - ENROLLED STUDENTS")
    password = st.text_input("ENTER PASSWORD",type="password")
    if password == "admin1234":
        import pandas as pd 
        conn = sqlite3.connect("student.db")
        df = pd.read_sql_query("SELECT * FROM enrollments",conn)
        conn.close()
        if not df.empty:
            st.success("ENROLLED STUDENTS DATA:")
            st.dataframe(df)
        else:
            st.warning("NO STUDENTS HAS ENROLLED YET")    
    elif password:
        st.error("INCORRECT PASSWOPRD")
