"""Q3: MySQL Student-Course Analytics Engine
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Prints SQL for analytics; mysql-connector-python is optional for execution.
"""
QUERIES = {
    "course_enrollment": """
        SELECT c.course_name, COUNT(e.student_id) AS enrollment_count
        FROM courses c LEFT JOIN enrollments e ON e.course_id = c.course_id
        GROUP BY c.course_id, c.course_name
        ORDER BY enrollment_count DESC, c.course_name;
    """,
    "student_average": """
        SELECT s.student_id, s.student_name, AVG(e.grade) AS average_grade
        FROM students s JOIN enrollments e ON e.student_id = s.student_id
        GROUP BY s.student_id, s.student_name
        ORDER BY average_grade DESC;
    """
}

def run_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()

if __name__ == "__main__":
    for name, query in QUERIES.items():
        print(f"--- {name} ---\n{query.strip()}")
