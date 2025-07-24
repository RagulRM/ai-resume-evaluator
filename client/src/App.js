import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jd', jd);

    try {
      const response = await axios.post('http://localhost:5000/evaluate', formData);
      setResult(response.data);
    } catch (error) {
      console.error("Error evaluating resume:", error);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🚀 AI Resume Evaluator</h1>
      <p>Upload your resume and job description:</p>

      <input type="file" onChange={(e) => setResume(e.target.files[0])} />
      <br /><br />
      <input type="file" onChange={(e) => setJd(e.target.files[0])} />
      <br /><br />
      <button onClick={handleSubmit}>Evaluate</button>

      {result && (
        <div style={{ marginTop: 30 }}>
          <h2>Score: {result.score}%</h2>
          <p><strong>Missing Skills:</strong> {result.missing_skills.join(', ')}</p>
        </div>
      )}
    </div>
  );
}

export default App;
