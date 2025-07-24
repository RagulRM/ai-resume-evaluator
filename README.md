# 🧠 AI Resume Evaluator

A simple AI-powered web app that evaluates how well your resume matches a job description. Built using **Python Flask** for the backend and **React** for the frontend.

---

## 🚀 Features

✅ Upload your Resume and Job Description  
✅ Get a Match Score (%)  
✅ View Missing Skills  
✅ Simple, Responsive UI  

---

## 🛠 Tech Stack

- **Frontend**: React.js  
- **Backend**: Python Flask  
- **AI/NLP**: spaCy  
- **PDF Parsing**: PyMuPDF  

---

## 📦 Project Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-resume-evaluator.git
cd ai-resume-evaluator
```

### 2️⃣ Backend Setup (Flask + Python)

#### 📁 Navigate to the server folder:
```bash
cd server
```

#### 🔒 Create and activate virtual environment (for Windows):
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🧑‍💻 On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 📦 Install dependencies:
```bash
pip install -r requirements.txt
```
#### ✅ requirements.txt should contain:
```nginx
Flask
python-dotenv
PyMuPDF
spacy
flask-cors
```

#### 📚 Download the spaCy model (only once):

```bash
python -m spacy download en_core_web_sm
```

### ▶️ Run the Flask server:

```bash
python app.py
```
🌐 Your backend is running at: http://127.0.0.1:5000
