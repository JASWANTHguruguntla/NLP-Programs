import re
for i in range(0,7):
  file_path = "./res"+str(i)+".txt"
  print()

  with open(file_path, "r", encoding="utf-8") as file:
    resume_text = file.read()
  words = resume_text.splitlines()
  name = words[0] if words else "No name found"
  email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  email = re.search(email_pattern, resume_text)
  email = email.group(0) if email else "No email found"
  phone_pattern = r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b'
  phone = re.search(phone_pattern, resume_text)
  phone = phone.group(0) if phone else "No phone number found"
  if name != "No name found" and email != "No email found" and phone != "No phone number found":
    decision = "Sorry, you are not selected for the interview."
  else:
    decision = "Congratulations, you are selected for the interview!"
  print(f"Name: {name}")
  print(f"Email: {email}")
  print(f"Phone: {phone}")
  print(f"Decision: {decision}",)
