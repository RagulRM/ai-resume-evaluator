# 🚀 AI Resume Evaluator - Deployment Guide

This guide will help you deploy your AI Resume Evaluator to various hosting platforms.

## 🎯 Pre-deployment Checklist

1. **Build the React App**
   ```bash
   cd client
   npm run build
   ```

2. **Test the Backend**
   ```bash
   cd server
   python app.py
   ```

3. **Environment Variables**
   Create a `.env` file in your server directory for production settings.

---

## 🌐 Frontend Deployment Options

### 1. Vercel (Recommended for Frontend)

**Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. In the `client` directory, run: `vercel`
3. Follow the prompts
4. Your site will be live at: `https://your-app.vercel.app`

**Configuration:**
Create `vercel.json` in the client directory:
```json
{
  "name": "ai-resume-evaluator",
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": { "distDir": "build" }
    }
  ],
  "routes": [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}
```

### 2. Netlify

**Steps:**
1. Build your app: `npm run build`
2. Drag and drop the `build` folder to Netlify
3. Or connect your GitHub repo for auto-deployment

### 3. GitHub Pages

**Steps:**
1. Install gh-pages: `npm install --save-dev gh-pages`
2. Add to package.json scripts:
   ```json
   "predeploy": "npm run build",
   "deploy": "gh-pages -d build"
   ```
3. Run: `npm run deploy`

---

## 🖥️ Backend Deployment Options

### 1. Railway (Recommended)

**Steps:**
1. Create account at railway.app
2. Connect your GitHub repo
3. Create `railway.toml`:
```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "python app.py"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

### 2. Render

**Steps:**
1. Create account at render.com
2. Connect your GitHub repo
3. Choose "Web Service"
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

### 3. Heroku

**Steps:**
1. Create `Procfile` in server directory:
   ```
   web: python app.py
   ```
2. Create `runtime.txt`:
   ```
   python-3.11.0
   ```
3. Deploy via Heroku CLI or GitHub integration

---

## 🔗 Full-Stack Deployment (Frontend + Backend)

### Option 1: Separate Hosting
- **Frontend**: Vercel/Netlify
- **Backend**: Railway/Render
- **Pros**: Better performance, scalability
- **Cons**: Need to manage CORS

### Option 2: Single Platform
Use platforms like Railway or Render that support both:

**Project Structure for Railway:**
```
├── client/          # React app
├── server/          # Flask app
└── railway.toml     # Configuration
```

---

## ⚙️ Environment Configuration

### Frontend (.env in client/)
```env
REACT_APP_API_URL=https://your-backend-domain.com
REACT_APP_ENV=production
```

### Backend (.env in server/)
```env
FLASK_ENV=production
PORT=5000
CORS_ORIGINS=https://your-frontend-domain.com
```

---

## 🔒 Security & Performance

### Backend Updates for Production:
```python
# app.py updates
from flask_cors import CORS
import os

app = Flask(__name__)

# Configure CORS for production
if os.getenv('FLASK_ENV') == 'production':
    CORS(app, origins=[os.getenv('CORS_ORIGINS')])
else:
    CORS(app)  # Allow all origins in development

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Frontend Updates:
Update API calls to use environment variable:
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
const response = await axios.post(`${API_URL}/evaluate`, formData);
```

---

## 🎨 Custom Domain Setup

### For Vercel:
1. Go to Project Settings > Domains
2. Add your custom domain
3. Update DNS records as instructed

### For Netlify:
1. Go to Site Settings > Domain Management
2. Add custom domain
3. Configure DNS

---

## 📊 Monitoring & Analytics

Consider adding:
- **Google Analytics** for user tracking
- **Sentry** for error monitoring
- **Hotjar** for user experience insights

---

## 🚨 Troubleshooting

### Common Issues:

1. **CORS Errors**: Update backend CORS configuration
2. **Build Failures**: Check Node.js version compatibility
3. **API Not Found**: Verify environment variables
4. **File Upload Issues**: Check file size limits on hosting platform

### Performance Optimization:

1. **Code Splitting**: Already handled by Create React App
2. **Image Optimization**: Use WebP format for images
3. **Caching**: Configure proper cache headers
4. **CDN**: Use platform's built-in CDN

---

## 🎉 Go Live!

Once deployed, your AI Resume Evaluator will be accessible worldwide! 

**Recommended Stack:**
- **Frontend**: Vercel (vercel.com)
- **Backend**: Railway (railway.app)
- **Domain**: Namecheap/GoDaddy
- **Monitoring**: Vercel Analytics + Railway Logs

Your users will now be able to access your cool AI Resume Evaluator from anywhere! 🌍✨
