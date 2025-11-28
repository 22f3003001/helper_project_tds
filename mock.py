from flask import Flask, send_from_directory, Response, send_file
from werkzeug.utils import safe_join
import os

app = Flask(__name__)

# Path to folder containing PDFs
PDF_FOLDER = os.path.join(os.path.dirname(__file__), "pdfs")
os.makedirs(PDF_FOLDER, exist_ok=True)  # create if not exists

HTML_CONTENT = """<!DOCTYPE html>
<html>
<body>
  <h1>Mock Data Analysis Question</h1>
  <p>Download the dataset and answer the question:</p>
  <p><b>Question:</b> Which branch has the highest revenue in first 3 months </p>
  <p>Dataset: <a href="/pdf">sample.pdf</a></p>
  <p>Submit your answer here: https://mock-submit.local/submit</p>
</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML_CONTENT, mimetype="text/html")

@app.route("/pdf")
def serve_pdf():
    file_path = "fake_company_report.pdf"  # must exist in same folder
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='application/pdf')
    return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




