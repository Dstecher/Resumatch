import fitz
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    return text

def analyze_resume(text):
    prompt = f"""
    You are a career coach. Your task is to analyze a resume and give some
    output directed to the person you can find in the resume directly.
    Please address them personally using their first name in the resume.
    Be honest and critical, still stay friendly and helpful when giving
    potentially guiding information to the customer.
    In the end, make sure to not include any formalities and regards or any
    farewell message to the customer, your output is a text integrated into a
    web app.
    Please analyze the following text from a resume:
    {text}

    1. List the most important hard and soft skills from the resume
    2. Recommend the 3 best IT job roles based on those skills
    3. List 2 skills, that are missing for those job opportunities
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
