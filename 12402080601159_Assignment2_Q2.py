"""Q2: Offline Web Scraping Ranker from HTML Pages
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Works offline using HTML strings and Python's standard library.
"""
from html.parser import HTMLParser
from collections import Counter
import re

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.parts.append(cleaned)

def page_text(html):
    parser = TextExtractor()
    parser.feed(html)
    return " ".join(parser.parts)

def rank_pages(query, pages):
    terms = [t.lower() for t in re.findall(r"\w+", query)]
    results = []
    for name, html in pages.items():
        text = page_text(html).lower()
        words = Counter(re.findall(r"\w+", text))
        score = sum(words[t] for t in terms)
        results.append({"page": name, "score": score})
    return sorted(results, key=lambda row: (-row["score"], row["page"]))

if __name__ == "__main__":
    pages = {"python.html": "<h1>Python</h1><p>Python supports scripting.</p>",
             "sql.html": "<h1>SQL</h1><p>SQL queries databases.</p>"}
    print(rank_pages("python scripting", pages))
