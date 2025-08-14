from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from models.resume_matcher import ResumeSkillMatcher
except ImportError:
    # Fallback for deployment
    import importlib.util
    spec = importlib.util.spec_from_file_location("resume_matcher", 
                                                  os.path.join(os.path.dirname(__file__), '..', 'models', 'resume_matcher.py'))
    resume_matcher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resume_matcher)
    ResumeSkillMatcher = resume_matcher.ResumeSkillMatcher

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Resume Evaluator API is running!", "status": "healthy"})

@app.route('/api/evaluate', methods=['POST'])
def evaluate_resume():
    try:
        if 'resume' not in request.files or 'job_description' not in request.files:
            return jsonify({
                'error': 'Both resume and job description files are required'
            }), 400
        
        resume_file = request.files['resume']
        job_file = request.files['job_description']
        
        if not resume_file.filename.endswith('.pdf') or not job_file.filename.endswith('.pdf'):
            return jsonify({
                'error': 'Only PDF files are supported'
            }), 400
        
        # Save files temporarily
        resume_path = f"/tmp/{resume_file.filename}"
        job_path = f"/tmp/{job_file.filename}"
        
        resume_file.save(resume_path)
        job_file.save(job_path)
        
        # Process files
        matcher = ResumeSkillMatcher()
        result = matcher.match_skills(resume_path, job_path)
        
        # Clean up files
        try:
            os.remove(resume_path)
            os.remove(job_path)
        except:
            pass  # Continue even if cleanup fails
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

# This is required for Vercel
app_instance = app

if __name__ == '__main__':
    app.run(debug=False)