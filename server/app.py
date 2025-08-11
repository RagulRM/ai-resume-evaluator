from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from models.resume_matcher import process_resume_and_jd

app = Flask(__name__)

# Configure CORS for production
if os.getenv('FLASK_ENV') == 'production':
    CORS(app, origins=[os.getenv('CORS_ORIGINS', '*')])
else:
    CORS(app)  # Allow all origins in development

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "AI Resume Evaluator API is running",
        "version": "1.0.0"
    })

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        if 'resume' not in request.files or 'jd' not in request.files:
            return jsonify({"error": "Both resume and job description files are required"}), 400
        
        resume_file = request.files['resume']
        jd_file = request.files['jd']
        
        if resume_file.filename == '' or jd_file.filename == '':
            return jsonify({"error": "Please select valid files"}), 400
        
        # Check file types
        if not (resume_file.filename.endswith('.pdf') and jd_file.filename.endswith('.pdf')):
            return jsonify({"error": "Only PDF files are supported"}), 400

        resume_path = os.path.join(UPLOAD_FOLDER, f"resume_{resume_file.filename}")
        jd_path = os.path.join(UPLOAD_FOLDER, f"jd_{jd_file.filename}")

        resume_file.save(resume_path)
        jd_file.save(jd_path)

        result = process_resume_and_jd(resume_path, jd_path)
        
        # Clean up files after processing
        try:
            os.remove(resume_path)
            os.remove(jd_path)
        except:
            pass  # Continue even if cleanup fails
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
