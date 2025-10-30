# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    
    # Mock response — later, connect to OpenAI or SharePoint files
    if "policy" in question.lower():
        answer = "Our company PTO policy allows 20 days of annual leave."
    else:
        answer = f"I'll search your SharePoint files for: {question}"

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
