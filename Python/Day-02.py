# ==========================================
# DAY 02 — LIST, TUPLE, SET & DICTIONARY
# ==========================================


print("========== LIST ==========")

programming_languages = ["Python", "C", "Java", "JavaScript"]

print("Programming Languages:", programming_languages)

programming_languages.append("Go")

print("Updated List:", programming_languages)

print("First Language:", programming_languages[0])


print("\n========== TUPLE ==========")

student_details = ("Leela Prasath", 19, "Chennai")

print("Student Details:", student_details)

print("Student Name:", student_details[0])


print("\n========== SET ==========")

ai_tools = {"ChatGPT", "Claude", "Gemini", "ChatGPT"}

print("AI Tools:", ai_tools)

# Adding new item
ai_tools.add("Copilot")

print("Updated Set:", ai_tools)


print("\n========== DICTIONARY ==========")

student_profile = {
    "name": "Leela Prasath",
    "age": 19,
    "department": "CSE",
    "goal": "AI Engineer"
}

print("Student Profile:", student_profile)

print("Name:", student_profile["name"])
print("Department:", student_profile["department"])

student_profile["age"] = 20

print("Updated Profile:", student_profile)

print("\n========== DATA TYPES ==========")

print("Type of List:", type(programming_languages))
print("Type of Tuple:", type(student_details))
print("Type of Set:", type(ai_tools))
print("Type of Dictionary:", type(student_profile))

print("\n========== PROGRAM COMPLETED ==========")
