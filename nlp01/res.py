import re
# Specify the file path
for i in range(0,2):
  if(i==0):
        file_path = "./res.txt"
  else :
        print("")
        file_path = "./res1.txt"
# Read the resume text from the file
  with open(file_path, "r", encoding="utf-8") as file:
    resume_text = file.read()

# Split text into lines
  words = resume_text.splitlines()
  name = words[0] if words else "No name found"

# Extract email
  email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  email = re.search(email_pattern, resume_text)
  email = email.group(0) if email else "No email found"

# Extract phone number
  phone_pattern = r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b'
  phone = re.search(phone_pattern, resume_text)
  phone = phone.group(0) if phone else "No phone number found"

# Decision logic
  if name != "No name found" and email != "No email found" and phone != "No phone number found":
    decision = "Sorry, you are not selected for the interview."
  else:
    decision = "Congratulations, you are selected for the interview!"

# Print extracted information
  print(f"Name: {name}")
  print(f"Email: {email}")
  print(f"Phone: {phone}")
  print(f"Decision: {decision}" ,)

import re

# Specify the file path
for i in range(0,2):
  if(i==0):
        file_path = "./res.txt"
  else :
        print("")
        file_path = "./res1.txt"
# Read the resume text from the file
  with open(file_path, "r", encoding="utf-8") as file:
    resume_text = file.read()

# Split text into lines
  words = resume_text.splitlines()
  name = words[0] if words else "No name found"

# Extract email
  email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  email = re.search(email_pattern, resume_text)
  email = email.group(0) if email else "No email found"

# Extract phone number
  phone_pattern = r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b'
  phone = re.search(phone_pattern, resume_text)
  phone = phone.group(0) if phone else "No phone number found"

# Decision logic
  if name != "No name found" and email != "No email found" and phone != "No phone number found":
    decision = "Sorry, you are not selected for the interview."
  else:
    decision = "Congratulations, you are selected for the interview!"

# Print extracted information
  print(f"Name: {name}")
  print(f"Email: {email}")
  print(f"Phone: {phone}")
  print(f"Decision: {decision}" ,)


