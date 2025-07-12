import json
from pathlib import Path

# Load JSON report
with open("semgrep-report.json", "r") as f:
    data = json.load(f)

# Prepare HTML structure
html = """<html>
<head>
    <title>Semgrep Report</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Semgrep Scan Report</h1>
    <table>
        <tr>
            <th>File Path</th>
            <th>Line</th>
            <th>Message</th>
            <th>Severity</th>
            <th>Rule</th>
        </tr>
"""

# Fill table rows
for result in data.get("results", []):
    path = result.get("path")
    line = result.get("start", {}).get("line")
    msg = result.get("extra", {}).get("message", "").replace("\n", " ")
    severity = result.get("extra", {}).get("severity", "N/A")
    rule = result.get("check_id", "N/A")

    html += f"""
        <tr>
            <td>{path}</td>
            <td>{line}</td>
            <td>{msg}</td>
            <td>{severity}</td>
            <td>{rule}</td>
        </tr>
    """

html += """
    </table>
</body>
</html>
"""

# Write to output file
Path("semgrep-reports").mkdir(exist_ok=True)
with open("semgrep-reports/index.html", "w") as f:
    f.write(html)

print("Semgrep HTML report generated: semgrep-reports/index.html")
