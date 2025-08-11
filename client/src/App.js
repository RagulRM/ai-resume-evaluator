import React, { useState, useRef } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [dragActive, setDragActive] = useState({ resume: false, jd: false });
  const resumeRef = useRef();
  const jdRef = useRef();

  const handleDrag = (e, type) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive({ ...dragActive, [type]: true });
    } else if (e.type === "dragleave") {
      setDragActive({ ...dragActive, [type]: false });
    }
  };

  const handleDrop = (e, type) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive({ ...dragActive, [type]: false });
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0];
      if (type === 'resume') {
        setResume(file);
      } else {
        setJd(file);
      }
    }
  };

  const handleSubmit = async () => {
    if (!resume || !jd) {
      alert('Please upload both resume and job description');
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jd', jd);

    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

    try {
      const response = await axios.post(`${API_URL}/evaluate`, formData);
      setResult(response.data);
    } catch (error) {
      console.error("Error evaluating resume:", error);
      alert('Error evaluating resume. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 80) return '#00ff88';
    if (score >= 60) return '#ffaa00';
    return '#ff4757';
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <div className="logo">
            <span className="rocket">🚀</span>
            <h1>AI Resume Evaluator</h1>
          </div>
          <p className="subtitle">Unlock your potential with AI-powered resume analysis</p>
        </header>

        <div className="upload-section">
          <div className="upload-grid">
            {/* Resume Upload */}
            <div 
              className={`upload-zone ${dragActive.resume ? 'drag-active' : ''} ${resume ? 'has-file' : ''}`}
              onDragEnter={(e) => handleDrag(e, 'resume')}
              onDragLeave={(e) => handleDrag(e, 'resume')}
              onDragOver={(e) => handleDrag(e, 'resume')}
              onDrop={(e) => handleDrop(e, 'resume')}
              onClick={() => resumeRef.current?.click()}
            >
              <div className="upload-content">
                <div className="upload-icon">📄</div>
                <h3>Resume</h3>
                <p>{resume ? resume.name : 'Drop your resume here or click to browse'}</p>
                <input
                  ref={resumeRef}
                  type="file"
                  accept=".pdf"
                  onChange={(e) => setResume(e.target.files[0])}
                  style={{ display: 'none' }}
                />
              </div>
            </div>

            {/* Job Description Upload */}
            <div 
              className={`upload-zone ${dragActive.jd ? 'drag-active' : ''} ${jd ? 'has-file' : ''}`}
              onDragEnter={(e) => handleDrag(e, 'jd')}
              onDragLeave={(e) => handleDrag(e, 'jd')}
              onDragOver={(e) => handleDrag(e, 'jd')}
              onDrop={(e) => handleDrop(e, 'jd')}
              onClick={() => jdRef.current?.click()}
            >
              <div className="upload-content">
                <div className="upload-icon">📋</div>
                <h3>Job Description</h3>
                <p>{jd ? jd.name : 'Drop job description here or click to browse'}</p>
                <input
                  ref={jdRef}
                  type="file"
                  accept=".pdf"
                  onChange={(e) => setJd(e.target.files[0])}
                  style={{ display: 'none' }}
                />
              </div>
            </div>
          </div>

          <button 
            className={`evaluate-btn ${loading ? 'loading' : ''}`}
            onClick={handleSubmit}
            disabled={loading || !resume || !jd}
          >
            {loading ? (
              <span className="loading-content">
                <div className="spinner"></div>
                Analyzing...
              </span>
            ) : (
              'Analyze Match'
            )}
          </button>
        </div>

        {result && (
          <div className="results-section">
            <div className="score-card">
              <div className="score-circle">
                <svg className="score-ring" viewBox="0 0 100 100">
                  <circle
                    className="score-background"
                    cx="50"
                    cy="50"
                    r="45"
                    fill="none"
                    stroke="rgba(255,255,255,0.1)"
                    strokeWidth="8"
                  />
                  <circle
                    className="score-progress"
                    cx="50"
                    cy="50"
                    r="45"
                    fill="none"
                    stroke={getScoreColor(result.score)}
                    strokeWidth="8"
                    strokeLinecap="round"
                    style={{
                      strokeDasharray: `${result.score * 2.83} 283`,
                      transform: 'rotate(-90deg)',
                      transformOrigin: '50px 50px'
                    }}
                  />
                </svg>
                <div className="score-text">
                  <span className="score-number">{result.score}%</span>
                  <span className="score-label">Match</span>
                </div>
              </div>
              {result.total_jd_skills && (
                <div className="score-details">
                  <p>Matched {result.total_matched} out of {result.total_jd_skills} required skills</p>
                </div>
              )}
            </div>

            <div className="skills-overview">
              {result.skill_categories && (
                <div className="skill-categories">
                  <h3>🎯 Skills by Category</h3>
                  <div className="category-grid">
                    {result.skill_categories.programming.length > 0 && (
                      <div className="category-card">
                        <h4>💻 Programming</h4>
                        <div className="category-skills">
                          {result.skill_categories.programming.map((skill, index) => (
                            <span key={index} className="skill-badge programming">{skill}</span>
                          ))}
                        </div>
                      </div>
                    )}
                    {result.skill_categories.frameworks.length > 0 && (
                      <div className="category-card">
                        <h4>🔧 Frameworks</h4>
                        <div className="category-skills">
                          {result.skill_categories.frameworks.map((skill, index) => (
                            <span key={index} className="skill-badge frameworks">{skill}</span>
                          ))}
                        </div>
                      </div>
                    )}
                    {result.skill_categories.cloud.length > 0 && (
                      <div className="category-card">
                        <h4>☁️ Cloud & DevOps</h4>
                        <div className="category-skills">
                          {result.skill_categories.cloud.map((skill, index) => (
                            <span key={index} className="skill-badge cloud">{skill}</span>
                          ))}
                        </div>
                      </div>
                    )}
                    {result.skill_categories.databases.length > 0 && (
                      <div className="category-card">
                        <h4>🗄️ Databases</h4>
                        <div className="category-skills">
                          {result.skill_categories.databases.map((skill, index) => (
                            <span key={index} className="skill-badge databases">{skill}</span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>

            <div className="skills-grid">
              {result.matched_skills.length > 0 && (
                <div className="skills-card matched">
                  <h3>✅ Your Matching Skills</h3>
                  <div className="skills-tags">
                    {result.matched_skills.map((skill, index) => (
                      <span key={index} className="skill-tag matched">{skill}</span>
                    ))}
                  </div>
                </div>
              )}

              {result.missing_skills.length > 0 && (
                <div className="skills-card missing">
                  <h3>⚡ Skills to Develop</h3>
                  <div className="skills-tags">
                    {result.missing_skills.map((skill, index) => (
                      <span key={index} className="skill-tag missing">{skill}</span>
                    ))}
                  </div>
                  <div className="improvement-tip">
                    <p>💡 <strong>Pro Tip:</strong> Focus on the top skills first - they carry more weight in the analysis!</p>
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
