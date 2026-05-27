

print("========== LOOP PRACTICE SYSTEM ==========")


print("\n========== FOR LOOP ==========")

for i in range(1, 6):
    print("Python Practice Day", i)


print("\n========== LOOPING THROUGH LIST ==========")

programming_languages = ["Python", "Java", "C", "JavaScript"]

for language in programming_languages:
    print("Language:", language)



print("\n========== WHILE LOOP ==========")

count = 1

while count <= 5:
    print("Count Value:", count)
    count += 1

print("\n========== MULTIPLICATION TABLE ==========")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


print("\n========== EVEN NUMBERS ==========")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


print("\n========== SUM OF NUMBERS ==========")

total = 0

for i in range(1, 11):
    total += i

print("Sum from 1 to 10 is:", total)


# PROGRAM COMPLETED
# ==========================================

print("\n========== PROGRAM COMPLETED ==========")
