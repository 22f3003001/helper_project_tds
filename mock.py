from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

# Ensure PDF folder exists
PDF_FOLDER = os.path.join(os.path.dirname(__file__), "pdfs")
os.makedirs(PDF_FOLDER, exist_ok=True)

HTML_CONTENT = """<!DOCTYPE html>
<html>
<body>
  <h1>Mock Data Analysis Question</h1>
  <p>Download the dataset and answer the question:</p>
  <p><b>Question:</b> Which branch has the highest revenue in first 3 months </p>
  <p>Dataset: <a href="/pdf">sample.pdf</a></p>
  <p>Submit your answer via POST /submit</p>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML_CONTENT

@app.route("/pdf")
def serve_pdf():
    file_path = os.path.join(PDF_FOLDER, "fake_company_report.pdf")
    if os.path.exists(file_path):
        return send_file(file_path, mimetype="application/pdf")
    return "File not found", 404

@app.route("/submit", methods=["POST"])
def submit_answer():
    # Accept JSON payload like {"answer": "branch c"}
    data = request.get_json()
    if not data or "answer" not in data:
        return jsonify({"success": False, "message": "No answer provided"}), 400

    answer = data["answer"].strip().lower()
    correct = answer == "branch c".lower()
    return jsonify({"success": correct})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)








