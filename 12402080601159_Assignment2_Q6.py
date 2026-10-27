"""Q6: Log Anomaly Detector using Sliding Window
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Flags windows whose ERROR count meets a configurable threshold.
"""
from collections import deque

def detect_anomalies(lines, window_size=5, error_threshold=3):
    if window_size < 1 or error_threshold < 1:
        raise ValueError("window_size and error_threshold must be positive")
    window = deque()
    errors = 0
    findings = []
    for index, line in enumerate(lines, start=1):
        is_error = "ERROR" in line.upper()
        window.append((index, is_error))
        errors += int(is_error)
        if len(window) > window_size:
            _, removed_error = window.popleft()
            errors -= int(removed_error)
        if len(window) == window_size and errors >= error_threshold:
            findings.append({"line": index, "window_start": window[0][0], "errors": errors})
    return findings

if __name__ == "__main__":
    sample = ["INFO started", "ERROR timeout", "ERROR retry", "WARN slow", "ERROR failed"]
    print(detect_anomalies(sample, window_size=4, error_threshold=2))
