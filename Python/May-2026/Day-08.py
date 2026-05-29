# ==========================================
# DAY 08 — STRINGS & LISTS PRACTICE
# ==========================================

print("===== STUDENT SKILL TRACKER =====")


name = input("Enter your name: ")
skills = input("Enter your skills separated by commas: ")


skills_list = skills.split(",")


print("\n===== STUDENT DETAILS =====")

print("Name :", name.title())

print("Skills :", skills_list)


print("\nTotal Skills :", len(skills_list))


print("\n===== SKILL LIST =====")

for skill in skills_list:

    print("-", skill.strip().upper())


search_skill = input("\nEnter skill to search: ").lower()

found = False

for skill in skills_list:

    if skill.strip().lower() == search_skill:

        found = True


if found:

    print("Skill Found")

else:

    print("Skill Not Found")

print("\n===== PROGRAM COMPLETED =====")
