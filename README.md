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

#### ▶️ Run the Flask server:
```bash
python app.py
```
🌐 Your backend is running at: http://127.0.0.1:5000


### 3️⃣ Frontend Setup (React)

#### 🖥 Open a new terminal, then:
```bash
cd client
```
#### 📦 Install dependencies:
```bash
npm install
```

#### ▶️ Start the React app:
```bash
npm start
```
🌐 Your frontend is running at: http://localhost:3000


### 🎯 How to Use

#### Visit http://localhost:3000
<img width="1328" height="606" alt="image" src="https://github.com/user-attachments/assets/0eb39183-cf9d-446a-ae0c-edbcf804db26" />

#### Upload your Resume PDF
<img width="1910" height="921" alt="image" src="https://github.com/user-attachments/assets/a5612ac7-3e4d-4697-94f5-bd26355a32dc" />

#### Upload a Job Description PDF
<img width="1915" height="946" alt="image" src="https://github.com/user-attachments/assets/1ff5c1f4-e7b5-4ef3-abb1-ac3d5690cd2b" />

#### Click "Evaluate" Get your Match Score and view Missing Skills
<img width="1914" height="822" alt="image" src="https://github.com/user-attachments/assets/9ec6fe03-fca3-462e-bfe9-86c9edebb0ab" />
