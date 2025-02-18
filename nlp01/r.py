import nltk
import re
from nltk.tokenize import word_tokenize
keywords=["python","java","javascript","developer","engineer"]
def check_resume_for_keywords(resume,keywords):
    with open(resume,'r')as file:
        content=file.read()
        name=content.splitlines()[0]
        tokens=word_tokenize(content.lower())
    for i in keywords:
        if i in tokens:
            matches=True
            break
        else:
            matches=False
        if matches:
            print("congratulations","bharath","your resume is matched,you're shortlistd")
            print()
        else:
            print("sorry","bharath","you're not shortlisted")
            print()
resumes=[
    'Q:\\22701A3107\\NLP\\res.1.txt',
    'Q:\\22701A3107\\NLP\\res.2.txt',
    'Q:\\22701A3107\\NLP\\res.3.txt',
    'Q:\\22701A3107\\NLP\\res.4.txt'
    ]
for i in resumes:
    check_resume_for_keywords(i,keywords)

