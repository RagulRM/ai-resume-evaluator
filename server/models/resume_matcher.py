import fitz  # PyMuPDF
import spacy
import re
from collections import Counter

nlp = spacy.load("en_core_web_sm")

# Comprehensive technical skills database
TECHNICAL_SKILLS = {
    # Programming Languages
    'programming_languages': {
        'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'go', 'rust', 'kotlin', 
        'swift', 'php', 'ruby', 'scala', 'haskell', 'clojure', 'erlang', 'elixir', 'dart',
        'r', 'matlab', 'perl', 'shell', 'bash', 'powershell', 'purescript'
    },
    
    # Frameworks & Libraries
    'frameworks': {
        'react', 'angular', 'vue', 'svelte', 'django', 'flask', 'fastapi', 'spring', 
        'express', 'nodejs', 'nest', 'laravel', 'rails', 'asp.net', 'blazor', 'xamarin',
        'flutter', 'ionic', 'cordova', 'electron', 'next.js', 'nuxt', 'gatsby'
    },
    
    # Databases
    'databases': {
        'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'cassandra', 
        'dynamodb', 'sqlite', 'oracle', 'mssql', 'mariadb', 'couchdb', 'neo4j',
        'influxdb', 'clickhouse', 'snowflake', 'bigquery'
    },
    
    # Cloud & DevOps
    'cloud_devops': {
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'ansible', 
        'jenkins', 'gitlab', 'github', 'circleci', 'travis', 'heroku', 'vercel',
        'netlify', 'cloudflare', 'nginx', 'apache', 'linux', 'ubuntu', 'centos'
    },
    
    # Data Science & AI
    'data_ai': {
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy', 'matplotlib', 
        'seaborn', 'jupyter', 'spark', 'hadoop', 'kafka', 'airflow', 'mlflow',
        'opencv', 'nltk', 'spacy', 'transformers', 'bert', 'gpt'
    },
    
    # Web Technologies
    'web_tech': {
        'html', 'css', 'sass', 'scss', 'tailwind', 'bootstrap', 'webpack', 'vite',
        'babel', 'eslint', 'prettier', 'graphql', 'rest', 'api', 'soap', 'grpc',
        'websocket', 'oauth', 'jwt', 'cors', 'csrf'
    },
    
    # Tools & Platforms
    'tools': {
        'git', 'svn', 'jira', 'confluence', 'slack', 'teams', 'zoom', 'figma',
        'sketch', 'adobe', 'photoshop', 'illustrator', 'postman', 'insomnia',
        'vscode', 'intellij', 'eclipse', 'vim', 'emacs'
    },
    
    # Methodologies & Concepts
    'methodologies': {
        'agile', 'scrum', 'kanban', 'devops', 'cicd', 'tdd', 'bdd', 'microservices',
        'serverless', 'api-first', 'event-driven', 'clean-code', 'solid', 'dry',
        'mvp', 'mvc', 'mvvm', 'clean-architecture', 'hexagonal'
    },
    
    # Emerging Technologies
    'emerging': {
        'blockchain', 'cryptocurrency', 'nft', 'defi', 'web3', 'metaverse', 'ar', 
        'vr', 'iot', 'edge-computing', 'quantum', '5g', 'low-code', 'no-code'
    }
}

# Flatten all technical skills into one set
ALL_TECHNICAL_SKILLS = set()
for category in TECHNICAL_SKILLS.values():
    ALL_TECHNICAL_SKILLS.update(category)

# Common words to filter out (stop words + business terms)
STOP_WORDS = {
    'experience', 'years', 'work', 'working', 'knowledge', 'skills', 'ability', 
    'responsible', 'requirements', 'qualification', 'preferred', 'plus', 'bonus',
    'team', 'project', 'development', 'software', 'application', 'system', 'solution',
    'business', 'client', 'customer', 'user', 'management', 'process', 'design',
    'implementation', 'maintenance', 'support', 'documentation', 'testing', 'quality',
    'performance', 'security', 'scalability', 'reliability', 'availability', 'optimization',
    'integration', 'deployment', 'monitoring', 'troubleshooting', 'debugging',
    'collaboration', 'communication', 'leadership', 'mentor', 'training', 'learning',
    'innovation', 'improvement', 'best', 'practices', 'standards', 'guidelines',
    'procedures', 'policies', 'compliance', 'governance', 'risk', 'audit',
    'version', 'control', 'architecture', 'infrastructure', 'platform', 'environment',
    'tool', 'technology', 'framework', 'library', 'language', 'database',
    'server', 'client', 'frontend', 'backend', 'fullstack', 'mobile', 'web',
    'desktop', 'cloud', 'onpremise', 'hybrid', 'distributed', 'concurrent',
    'asynchronous', 'synchronous', 'realtime', 'batch', 'streaming', 'pipeline',
    'workflow', 'automation', 'manual', 'automated', 'continuous', 'delivery',
    'operations', 'production', 'staging', 'development', 'test', 'qa',
    'uat', 'acceptance', 'unit', 'integration', 'e2e', 'regression',
    'load', 'stress', 'penetration', 'vulnerability', 'authentication', 'authorization',
    'encryption', 'ssl', 'tls', 'https', 'http', 'tcp', 'udp', 'ip',
    'dns', 'cdn', 'load-balancer', 'proxy', 'gateway', 'firewall',
    'vpn', 'ssh', 'ftp', 'sftp', 'smtp', 'pop', 'imap',
    'json', 'xml', 'yaml', 'csv', 'pdf', 'excel', 'word',
    'powerpoint', 'presentation', 'report', 'dashboard', 'visualization',
    'analytics', 'metrics', 'kpi', 'roi', 'sla', 'slo', 'sli',
    'budget', 'cost', 'revenue', 'profit', 'loss', 'margin',
    'growth', 'scale', 'expand', 'migrate', 'upgrade', 'modernize',
    'legacy', 'greenfield', 'brownfield', 'poc', 'mvp', 'prototype',
    'research', 'analysis', 'design', 'architecture', 'planning',
    'estimation', 'roadmap', 'milestone', 'deadline', 'timeline',
    'schedule', 'resource', 'allocation', 'capacity', 'utilization',
    'efficiency', 'productivity', 'throughput', 'latency', 'response',
    'time', 'speed', 'fast', 'slow', 'quick', 'rapid', 'instant',
    'real', 'live', 'dynamic', 'static', 'interactive', 'responsive',
    'adaptive', 'flexible', 'robust', 'stable', 'mature', 'cutting',
    'edge', 'latest', 'modern', 'legacy', 'old', 'new', 'next',
    'generation', 'future', 'trend', 'industry', 'market', 'competitive',
    'advantage', 'differentiator', 'unique', 'innovative', 'creative',
    'problem', 'solving', 'solution', 'approach', 'strategy', 'tactical',
    'operational', 'strategic', 'technical', 'functional', 'non-functional',
    'requirement', 'specification', 'acceptance', 'criteria', 'definition',
    'scope', 'boundary', 'constraint', 'assumption', 'dependency', 'risk',
    'issue', 'blocker', 'impediment', 'challenge', 'opportunity', 'benefit',
    'value', 'impact', 'outcome', 'result', 'deliverable', 'artifact',
    'document', 'file', 'folder', 'directory', 'path', 'url', 'uri',
    'endpoint', 'service', 'api', 'interface', 'contract', 'protocol',
    'standard', 'convention', 'pattern', 'anti-pattern', 'best-practice',
    'worst-practice', 'lesson', 'learned', 'retrospective', 'feedback',
    'review', 'approval', 'sign-off', 'go-live', 'launch', 'release',
    'rollback', 'rollout', 'deployment', 'installation', 'configuration',
    'setup', 'initialization', 'startup', 'shutdown', 'restart', 'reload',
    'refresh', 'sync', 'backup', 'restore', 'recovery', 'disaster',
    'prevention', 'mitigation', 'contingency', 'plan', 'procedure', 'checklist',
    'runbook', 'playbook', 'handbook', 'manual', 'guide', 'tutorial',
    'training', 'workshop', 'seminar', 'conference', 'meetup', 'networking',
    'community', 'forum', 'blog', 'article', 'paper', 'research', 'study',
    'case', 'example', 'sample', 'demo', 'proof', 'concept', 'pilot',
    'trial', 'experiment', 'hypothesis', 'validation', 'verification',
    'certification', 'accreditation', 'license', 'permit', 'approval',
    'compliance', 'regulation', 'law', 'legal', 'ethical', 'moral',
    'social', 'environmental', 'sustainability', 'green', 'carbon',
    'footprint', 'neutral', 'offset', 'renewable', 'clean', 'efficient'
}

def extract_text(pdf_path):
    """Extract text from PDF with better formatting preservation"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def clean_and_normalize_text(text):
    """Clean and normalize text for better processing"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters but keep hyphens and dots for tech terms
    text = re.sub(r'[^\w\s\-\.\+#]', ' ', text)
    
    # Handle common variations
    replacements = {
        'node.js': 'nodejs',
        'next.js': 'nextjs',
        'vue.js': 'vue',
        'react.js': 'react',
        'angular.js': 'angular',
        'c++': 'cpp',
        'c#': 'csharp',
        '.net': 'dotnet',
        'asp.net': 'aspnet',
        'sql server': 'mssql',
        'postgresql': 'postgres',
        'amazon web services': 'aws',
        'google cloud platform': 'gcp',
        'microsoft azure': 'azure',
        'machine learning': 'ml',
        'artificial intelligence': 'ai',
        'natural language processing': 'nlp',
        'computer vision': 'cv',
        'deep learning': 'dl',
        'continuous integration': 'ci',
        'continuous deployment': 'cd',
        'test driven development': 'tdd',
        'behavior driven development': 'bdd',
        'user interface': 'ui',
        'user experience': 'ux',
        'application programming interface': 'api',
        'representational state transfer': 'rest',
        'software development kit': 'sdk',
        'integrated development environment': 'ide',
        'version control system': 'vcs',
        'content management system': 'cms',
        'customer relationship management': 'crm',
        'enterprise resource planning': 'erp',
        'extract transform load': 'etl',
        'business intelligence': 'bi',
        'key performance indicator': 'kpi',
        'return on investment': 'roi',
        'service level agreement': 'sla',
        'minimum viable product': 'mvp',
        'proof of concept': 'poc',
        'research and development': 'rd',
        'quality assurance': 'qa',
        'user acceptance testing': 'uat',
        'end to end': 'e2e'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def extract_technical_skills(text):
    """Extract technical skills using multiple approaches"""
    text = clean_and_normalize_text(text)
    
    skills = set()
    
    # Method 1: Direct matching with technical skills database
    words = re.findall(r'\b\w+(?:[-\.]\w+)*\b', text)
    for word in words:
        if word in ALL_TECHNICAL_SKILLS and word not in STOP_WORDS:
            skills.add(word)
    
    # Method 2: Multi-word technical terms
    multi_word_skills = {
        'machine learning', 'deep learning', 'computer vision', 'natural language processing',
        'data science', 'big data', 'cloud computing', 'edge computing', 'quantum computing',
        'blockchain technology', 'artificial intelligence', 'augmented reality', 'virtual reality',
        'internet of things', 'cyber security', 'information security', 'network security',
        'mobile development', 'web development', 'full stack', 'front end', 'back end',
        'devops engineering', 'site reliability', 'platform engineering', 'infrastructure engineering',
        'software architecture', 'system design', 'database design', 'api design',
        'user interface', 'user experience', 'product management', 'project management',
        'agile methodology', 'scrum master', 'product owner', 'business analyst',
        'data analyst', 'data engineer', 'software engineer', 'systems engineer',
        'security engineer', 'network engineer', 'cloud engineer', 'platform engineer'
    }
    
    for skill in multi_word_skills:
        if skill in text:
            # Add the main term (last word usually)
            main_term = skill.split()[-1]
            if main_term in ALL_TECHNICAL_SKILLS:
                skills.add(main_term)
    
    # Method 3: NLP-based extraction for technical terms
    doc = nlp(text)
    for token in doc:
        if (token.pos_ in ['NOUN', 'PROPN'] and 
            not token.is_stop and 
            len(token.text) > 2 and
            token.lemma_.lower() in ALL_TECHNICAL_SKILLS and
            token.lemma_.lower() not in STOP_WORDS):
            skills.add(token.lemma_.lower())
    
    # Method 4: Pattern matching for version numbers and specific formats
    version_patterns = [
        r'\b(python|java|node|php|ruby|go|rust)\s*\d+(?:\.\d+)*\b',
        r'\b(aws|azure|gcp)[\s\-]?\w+\b',
        r'\b(spring|django|react|angular|vue)[\s\-]?\w*\b'
    ]
    
    for pattern in version_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]
            if match.lower() in ALL_TECHNICAL_SKILLS:
                skills.add(match.lower())
    
    return skills

def calculate_skill_importance_weights():
    """Calculate weights for different skill categories"""
    weights = {
        'programming_languages': 3.0,  # Most important
        'frameworks': 2.5,
        'databases': 2.0,
        'cloud_devops': 2.5,
        'data_ai': 2.0,
        'web_tech': 1.5,
        'tools': 1.0,  # Least important
        'methodologies': 1.5,
        'emerging': 2.0
    }
    return weights

def get_skill_category(skill):
    """Get the category of a skill for weighting"""
    for category, skills in TECHNICAL_SKILLS.items():
        if skill in skills:
            return category
    return 'tools'  # Default category

def calculate_weighted_score(matched_skills, jd_skills):
    """Calculate weighted score based on skill importance"""
    weights = calculate_skill_importance_weights()
    
    total_weight = 0
    matched_weight = 0
    
    for skill in jd_skills:
        category = get_skill_category(skill)
        weight = weights.get(category, 1.0)
        total_weight += weight
        
        if skill in matched_skills:
            matched_weight += weight
    
    if total_weight == 0:
        return 0
    
    return round((matched_weight / total_weight) * 100, 2)

def filter_relevant_skills(skills, context_text):
    """Filter skills based on context relevance"""
    filtered_skills = set()
    context_words = set(context_text.lower().split())
    
    for skill in skills:
        # Always include if it's a major technology
        if skill in {'python', 'java', 'javascript', 'react', 'aws', 'docker', 'kubernetes'}:
            filtered_skills.add(skill)
            continue
            
        # Check if skill appears in meaningful context
        skill_contexts = [
            f"{skill} development",
            f"{skill} programming",
            f"{skill} framework",
            f"{skill} experience",
            f"using {skill}",
            f"with {skill}",
            f"{skill} skills"
        ]
        
        for context in skill_contexts:
            if any(word in context_words for word in context.split()):
                filtered_skills.add(skill)
                break
    
    return filtered_skills

def process_resume_and_jd(resume_path, jd_path):
    """Enhanced resume and job description processing"""
    try:
        # Extract text
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)
        
        # Extract technical skills
        resume_skills = extract_technical_skills(resume_text)
        jd_skills = extract_technical_skills(jd_text)
        
        # Filter relevant skills based on context
        resume_skills = filter_relevant_skills(resume_skills, resume_text)
        jd_skills = filter_relevant_skills(jd_skills, jd_text)
        
        # Find matches
        matched_skills = resume_skills & jd_skills
        missing_skills = jd_skills - resume_skills
        
        # Calculate weighted score
        if len(jd_skills) == 0:
            score = 0
        else:
            score = calculate_weighted_score(matched_skills, jd_skills)
        
        # Sort skills by importance for better presentation
        def skill_sort_key(skill):
            category = get_skill_category(skill)
            weights = calculate_skill_importance_weights()
            return -weights.get(category, 1.0)  # Negative for descending order
        
        matched_skills_sorted = sorted(list(matched_skills), key=skill_sort_key)
        missing_skills_sorted = sorted(list(missing_skills), key=skill_sort_key)
        
        return {
            "score": score,
            "matched_skills": matched_skills_sorted[:20],  # Limit to top 20
            "missing_skills": missing_skills_sorted[:15],  # Limit to top 15
            "total_jd_skills": len(jd_skills),
            "total_matched": len(matched_skills),
            "skill_categories": {
                "programming": [s for s in matched_skills if s in TECHNICAL_SKILLS['programming_languages']],
                "frameworks": [s for s in matched_skills if s in TECHNICAL_SKILLS['frameworks']],
                "cloud": [s for s in matched_skills if s in TECHNICAL_SKILLS['cloud_devops']],
                "databases": [s for s in matched_skills if s in TECHNICAL_SKILLS['databases']]
            }
        }
        
    except Exception as e:
        return {
            "error": f"Error processing files: {str(e)}",
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }
