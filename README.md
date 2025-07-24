# 🚀 AI Resume Evaluator (React + Flask)

An AI-powered web app that evaluates your resume against a job description and provides:
- A **matching score** (percentage)
- A list of **missing skills**
  
Perfect for job seekers to tailor their resumes!

---

## 📁 Project Structure

resume-evaluator/
├── client/ # React frontend (UI)
├── server/ # Flask backend (AI processing)
├── README.md # You're reading this!
└── .gitignore
---

## ⚙️ Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Frontend   | React.js           |
| Backend    | Python + Flask     |
| NLP Engine | spaCy              |
| PDF Reader | PyMuPDF (`fitz`)   |

---

## 🧪 Features

- Upload **Resume (PDF)**
- Upload **Job Description (PDF)**
- Click “Evaluate”
- View your **Match Score** and **Missing Skills**

---

## 🚀 Getting Started

These steps help you run the project **locally** on your machine.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-resume-evaluator.git
cd ai-resume-evaluator
2️⃣ Backend Setup (Python + Flask)

Step 1: Go to server folder
cd server

Step 2: Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate
If you're on Mac/Linux, use:
python3 -m venv venv
source venv/bin/activate

Step 3: Install Python dependencies
pip install -r requirements.txt
Make sure requirements.txt includes:
Flask
python-dotenv
PyMuPDF
spacy
flask-cors

Step 4: Download spaCy model (only once)
python -m spacy download en_core_web_sm

Step 5: Run the backend server
python app.py
✅ Flask should run on: http://127.0.0.1:5000/

3️⃣ Frontend Setup (React)
Step 1: Open new terminal & go to client folder
cd ../client

Step 2: Install React dependencies
npm install

Step 3: Start React app
npm start
✅ React runs on: http://localhost:3000/

4️⃣ Usage Instructions
Open your browser and go to http://localhost:3000

Upload your Resume PDF

Upload the Job Description PDF

Click Evaluate

See your Match Score and Missing Skills
