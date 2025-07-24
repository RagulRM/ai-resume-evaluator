import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    return "".join([page.get_text() for page in doc])

def get_keywords(text):
    doc = nlp(text)
    return set([token.lemma_.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop])

def process_resume_and_jd(resume_path, jd_path):
    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)

    resume_keywords = get_keywords(resume_text)
    jd_keywords = get_keywords(jd_text)

    matched = resume_keywords & jd_keywords
    unmatched = jd_keywords - resume_keywords

    score = round((len(matched) / len(jd_keywords)) * 100, 2)

    return {
        "score": score,
        "matched_skills": list(matched),
        "missing_skills": list(unmatched)
    }
