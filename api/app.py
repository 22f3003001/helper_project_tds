from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get the current host URL dynamically
    base_url = request.host_url.rstrip('/')
    
    HTML_CONTENT = f"""<!DOCTYPE html>
<html>
<body>
  <h1>Mock Data Analysis Question</h1>
  <p>Download the dataset and answer the question:</p>
  <p><b>Question:</b> Which branch has the highest revenue in first 3 months?</p>
  <p>Dataset: <a href="/pdf">sample.pdf</a></p>
  <p>Submit your answer via POST to <code>{base_url}/submit</code></p>
</body>
</html>
"""
    return HTML_CONTENT

@app.route("/pdf")
def serve_pdf():
    # Path to PDF in same directory as app.py
    file_path = os.path.join(os.path.dirname(__file__), "fake_company_report.pdf")
    
    if os.path.exists(file_path):
        return send_file(file_path, mimetype="application/pdf")
    
    return jsonify({"error": "File not found"}), 404

@app.route("/submit", methods=["POST"])
def submit_answer():
    data = request.get_json()
    
    if not data or "answer" not in data:
        return jsonify({
            "correct": False,
            "reason": "No answer provided"
        }), 400
    
    answer = data["answer"].strip().lower()
    
    # Check if answer is "branch c" (case-insensitive)
    if answer == "branch c":
        return jsonify({
            "correct": True,
            "reason": None
        })
    else:
        return jsonify({
            "correct": False,
            "reason": "Incorrect answer"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)














