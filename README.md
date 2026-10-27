# Assignment 2 — Python Programs

**Student Name:** Yashvardhansinh Parmar  
**Enrollment Number:** 12402080601159

## Files
Each solution uses the enrollment-based naming convention:

- `12402080601159_Assignment2_Q1.py` — Regex-Based Email Intelligence Extractor
- `12402080601159_Assignment2_Q2.py` — Offline Web Scraping Ranker from HTML Pages
- `12402080601159_Assignment2_Q3.py` — MySQL Student-Course Analytics Engine
- `12402080601159_Assignment2_Q4.py` — SQL Join Query Builder and Validator
- `12402080601159_Assignment2_Q5.py` — Tkinter Contact Manager with MySQL Backend (UI demo)
- `12402080601159_Assignment2_Q6.py` — Log Anomaly Detector using Sliding Window
- `12402080601159_Assignment2_Q7.py` — Generator-Based JSON ETL Pipeline
- `12402080601159_Assignment2_Q8.py` — Matrix Path Optimizer with Dynamic Programming
- `12402080601159_Assignment2_Q9.py` — OOP Inventory Merger with Operator Overloading
- `12402080601159_Assignment2_Q10.py` — Python Data Visualization Dashboard Exporter

## Requirements
- Python 3.10+ recommended
- Most examples use only the Python standard library.
- Q10 requires `matplotlib`: `python -m pip install matplotlib`
- Q3 requires a configured MySQL database and `mysql-connector-python` only if you choose to execute the SQL:
  `python -m pip install mysql-connector-python`

## Run
Run any file from this folder, for example:

```bash
python 12402080601159_Assignment2_Q1.py
python 12402080601159_Assignment2_Q8.py
```

Q5 opens a Tkinter window. Q10 writes `dashboard.png` in the current directory.
Q3 prints example SQL statements and does not connect to a database automatically.

## Test examples
Run the included smoke tests with:

```bash
python test_examples.py
```

The tests use only the standard library and do not require MySQL or a GUI.
