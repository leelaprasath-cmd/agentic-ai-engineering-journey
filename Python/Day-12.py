# ==========================================
# DAY 12 — FILE HANDLING BASICS
# ==========================================

print("===== DAILY NOTES SAVER =====")

note = input("Enter your note: ")

# Write note to file
file = open("notes.txt", "w")

file.write(note)

file.close()

print("\nNote saved successfully!")

file = open("notes.txt", "r")

content = file.read()

file.close()

print("\n===== SAVED NOTE =====")
print(content)

print("\n===== PROGRAM COMPLETED =====")
