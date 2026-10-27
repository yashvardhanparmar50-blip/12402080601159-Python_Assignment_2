"""Q4: SQL Join Query Builder and Validator
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Builds a constrained SELECT/JOIN query from supplied identifiers.
"""
import re

IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

def validate_identifier(value):
    if not IDENTIFIER.fullmatch(value):
        raise ValueError(f"Invalid SQL identifier: {value!r}")
    return value

def build_join_query(table_a, table_b, key_a, key_b, columns="*"):
    a, b = map(validate_identifier, (table_a, table_b))
    ka, kb = map(validate_identifier, (key_a, key_b))
    if columns != "*":
        columns = ", ".join(validate_identifier(c.strip()) for c in columns.split(","))
    return (f"SELECT {columns} FROM {a} AS a "
            f"INNER JOIN {b} AS b ON a.{ka} = b.{kb};")

if __name__ == "__main__":
    print(build_join_query("students", "enrollments", "student_id", "student_id"))
