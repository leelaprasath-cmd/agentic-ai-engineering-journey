# ==========================================
# DAY 10 — SETS & TUPLES PRACTICE
# ==========================================

print("===== FAVORITE TECHNOLOGIES TRACKER =====")


student_info = (
    "Leela Prasath",
    "CSE",
    "AI Engineer"
)

print("\n===== STUDENT INFO =====")

print("Name       :", student_info[0])
print("Department :", student_info[1])
print("Goal       :", student_info[2])


technologies = {
    "Python",
    "Git",
    "Python",
    "Linux",
    "GitHub"
}

print("\n===== TECHNOLOGIES =====")

print(technologies)


new_tech = input("\nEnter a technology to add: ")

technologies.add(new_tech)

print("\nUpdated Technologies:")
print(technologies)


search_tech = input("\nEnter technology to search: ")

if search_tech in technologies:

    print("Technology Found")

else:

    print("Technology Not Found")


print("\nTotal Technologies :", len(technologies))


print("\n===== TECHNOLOGY LIST =====")

for tech in technologies:

    print("-", tech)


print("\n===== PROGRAM COMPLETED =====")
