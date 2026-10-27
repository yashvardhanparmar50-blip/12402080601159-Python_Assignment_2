"""Q7: Generator-Based JSON ETL Pipeline
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
"""
import json

def read_records(json_text):
    """Yield records from a JSON array or newline-delimited JSON."""
    stripped = json_text.strip()
    if not stripped:
        return
    if stripped.startswith("["):
        for record in json.loads(stripped):
            yield record
    else:
        for line in stripped.splitlines():
            if line.strip():
                yield json.loads(line)

def transform_records(records):
    for record in records:
        normalized = {str(k).strip().lower(): v for k, v in record.items()}
        if "name" in normalized:
            normalized["name"] = str(normalized["name"]).strip()
        yield normalized

def export_jsonl(records):
    return "\n".join(json.dumps(row, ensure_ascii=False) for row in records)

if __name__ == "__main__":
    source = '[{"Name":" Alice ","Score":9},{"Name":"Bob","Score":8}]'
    print(export_jsonl(transform_records(read_records(source))))
