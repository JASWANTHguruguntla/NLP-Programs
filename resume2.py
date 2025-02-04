import re
from collections import Counter
resume1 = """
pavan kumar is a Software Engineer proficient in Python, SQL, AWS, and Machine Learning. He has worked on several cloud-based systems.
He holds a B.S. in Computer Science from MIT. 
"""
job_desc1="""
i am a software developer
"""

resume2 = """
Neha sharma is a Data Scientist with expertise in Python, SQL, and Data Analysis. She has worked on various data projects but lacks experience in cloud technologies like AWS.
She graduated with a B.A. in Mathematics from Stanford.
"""
job_desc2="""
i am a software developer
"""
def extract_skills(text):
    skills = ['python', 'sql', 'aws', 'machine learning', 'data analysis', 'cloud', 'java', 'c++', 'teamwork', 'leadership']
    words = set(re.findall(r'\b\w+\b', text.lower()))
    matching_skills = words.intersection(set(skills))
    return matching_skills
def check_eligibility(resume, job_desc):
    job_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume)
    common_skills = resume_skills.intersection(job_skills)
    skill_match_percentage = len(common_skills) / len(job_skills) * 100 if job_skills else 0
    experience_match = "experience" in resume.lower()
    education_match = "computer science" in resume.lower() or "related field" in resume.lower()
    
    eligibility_score = skill_match_percentage
    if experience_match:
        eligibility_score += 20
    if education_match:
        eligibility_score += 20  
  
    print(f"Matching Skills: {common_skills}")
    print(f"Skill Match Percentage: {skill_match_percentage:.2f}%")
    print(f"Relevant Experience: {'Yes' if experience_match else 'No'}")
    print(f"Relevant Education: {'Yes' if education_match else 'No'}")
    print(f"Total Eligibility Score: {eligibility_score:.2f}%")
    eligibility="""
        eligible as software engineer
        """
    return eligibility
print("resume 1 eligibility:")
resume1_score = check_eligibility(resume1,job_desc1)
print("\nResume 2 Eligibility:")
resume2_score = check_eligibility(resume2, job_desc2)
print("\nEligibility Result:")
if resume1_score == True:
    print("Resume 1 is eligible for the job!")
else:
    print("Resume 1 is not eligible for the job!")

if resume2_score == True:
    print("Resume 2 is eligible for the job!")
else:
    print("Resume 2 is not eligible for the job!")
