# 🚀 AI Resume Evaluator

A cutting-edge, AI-powered web application that revolutionizes resume analysis. Built with modern technologies and featuring a stunning futuristic UI design.

<div align="center">

![AI Resume Evaluator](https://img.shields.io/badge/AI-Resume%20Evaluator-blueviolet?style=for-the-badge&logo=rocket)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask)

**Unlock your potential with AI-powered resume analysis**

</div>

---

## ✨ Features

🎯 **Smart AI Analysis** - Advanced NLP processing with spaCy  
📊 **Real-time Scoring** - Instant match percentage calculation  
🔍 **Skill Gap Analysis** - Identify missing skills and improvements  
🎨 **Futuristic UI** - Modern grid-based design with glassmorphism  
📱 **Fully Responsive** - Perfect on desktop, tablet, and mobile  
⚡ **Drag & Drop** - Intuitive file upload experience  
🔒 **Secure Processing** - Files are automatically cleaned after analysis  
🌐 **Production Ready** - Optimized for deployment on any platform  

---

## 🛠 Tech Stack

### Frontend
- **React 18+** - Modern React with hooks
- **CSS3** - Custom animations and grid layouts
- **Axios** - API communication
- **Inter Font** - Clean, modern typography

### Backend
- **Python 3.11+** - Latest Python features
- **Flask 2.0+** - Lightweight web framework
- **spaCy** - Advanced NLP processing
- **PyMuPDF** - Reliable PDF text extraction
- **Flask-CORS** - Cross-origin resource sharing

### AI/ML
- **spaCy en_core_web_sm** - English language model
- **NLP Algorithms** - Keyword extraction and matching
- **Statistical Analysis** - Percentage scoring system

---

## 🎨 Design Features

- **Grid Background** - Futuristic cyberpunk-inspired design
- **Glassmorphism** - Modern frosted glass effects
- **Smooth Animations** - Fluid transitions and hover effects
- **Color-coded Results** - Visual feedback with dynamic colors
- **Loading States** - Professional loading animations
- **Responsive Layout** - Mobile-first design approach

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
