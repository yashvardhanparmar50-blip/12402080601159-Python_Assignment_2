"""Q1: Regex-Based Email Intelligence Extractor
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
"""
import re
from collections import Counter

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

def extract_emails(text):
    emails = EMAIL_RE.findall(text)
    domains = Counter(email.rsplit("@", 1)[1].lower() for email in emails)
    return {"emails": emails, "count": len(emails), "domains": dict(domains)}

if __name__ == "__main__":
    sample = "Contact yash@example.com or support@example.org; invalid@address."
    print(extract_emails(sample))
