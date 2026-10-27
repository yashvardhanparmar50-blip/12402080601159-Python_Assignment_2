"""Q10: Python Data Visualization Dashboard Exporter
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Exports a simple bar chart to PNG using matplotlib.
Install: python -m pip install matplotlib
"""
def export_dashboard(labels, values, output_path="dashboard.png"):
    if len(labels) != len(values) or not labels:
        raise ValueError("labels and values must have the same non-zero length")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(labels, values)
    ax.set_title("Dashboard Summary")
    ax.set_ylabel("Value")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path

if __name__ == "__main__":
    print(export_dashboard(["Q1", "Q2", "Q3", "Q4"], [12, 18, 15, 23]))
