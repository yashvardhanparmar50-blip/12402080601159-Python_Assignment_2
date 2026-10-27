"""Smoke tests for Assignment 2 by Yashvardhansinh Parmar (12402080601159)."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent

def load(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class AssignmentExamples(unittest.TestCase):
    def test_q1_email_extraction(self):
        m = load("12402080601159_Assignment2_Q1.py", "q1")
        result = m.extract_emails("a@test.com and b@test.com")
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["domains"], {"test.com": 2})

    def test_q2_ranker(self):
        m = load("12402080601159_Assignment2_Q2.py", "q2")
        ranked = m.rank_pages("python", {"a": "<p>Python Python</p>", "b": "<p>SQL</p>"})
        self.assertEqual(ranked[0]["page"], "a")

    def test_q4_identifier_validation(self):
        m = load("12402080601159_Assignment2_Q4.py", "q4")
        self.assertIn("INNER JOIN", m.build_join_query("students", "courses", "id", "student_id"))
        with self.assertRaises(ValueError):
            m.validate_identifier("students; DROP TABLE")

    def test_q6_anomaly(self):
        m = load("12402080601159_Assignment2_Q6.py", "q6")
        lines = ["ERROR a", "INFO", "ERROR b"]
        self.assertTrue(m.detect_anomalies(lines, window_size=3, error_threshold=2))

    def test_q7_etl(self):
        m = load("12402080601159_Assignment2_Q7.py", "q7")
        rows = list(m.transform_records(m.read_records('[{"Name":" Alice "}]')))
        self.assertEqual(rows[0]["name"], "Alice")

    def test_q8_path(self):
        m = load("12402080601159_Assignment2_Q8.py", "q8")
        cost, path = m.minimum_path([[1, 2], [3, 4]])
        self.assertEqual(cost, 7)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (1, 1))

    def test_q9_inventory(self):
        m = load("12402080601159_Assignment2_Q9.py", "q9")
        self.assertEqual((m.Inventory({"pen": 2}) + m.Inventory({"pen": 3}))["pen"], 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
