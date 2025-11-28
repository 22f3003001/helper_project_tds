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
  <p>Dataset: <a href=`{base_url}/pdf`>sample.pdf</a></p>
  <p>Submit your answer via POST to <code>{base_url}/submit</code></p>
  
  <hr>
  <h3>Test Form (Optional):</h3>
  <form id="answerForm">
    <input type="text" id="answerInput" placeholder="Enter your answer">
    <button type="submit">Submit</button>
  </form>
  <div id="result"></div>
  
  <script>
    document.getElementById('answerForm').addEventListener('submit', async (e) => {{
      e.preventDefault();
      const answer = document.getElementById('answerInput').value;
      const response = await fetch(`{base_url}/submit`, {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{answer: answer}})
      }});
      const data = await response.json();
      document.getElementById('result').innerHTML = 
        data.success ? '<p style="color:green">✓ Correct!</p>' : '<p style="color:red">✗ Incorrect</p>';
    }});
  </script>
</body>
</html>
"""
    return HTML_CONTENT

@app.route("/pdf")
def serve_pdf():
    # Get the absolute path relative to the app.py file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level from 'api' folder to reach 'fake_company_report.pdf'
    file_path = os.path.join(current_dir, "..", "fake_company_report.pdf")
    
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
    correct = answer == "branch c"
    
    return jsonify({"success": correct})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)











