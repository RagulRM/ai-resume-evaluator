from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from models.resume_matcher import process_resume_and_jd

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    resume_file = request.files['resume']
    jd_file = request.files['jd']

    resume_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
    jd_path = os.path.join(UPLOAD_FOLDER, jd_file.filename)

    resume_file.save(resume_path)
    jd_file.save(jd_path)

    result = process_resume_and_jd(resume_path, jd_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
