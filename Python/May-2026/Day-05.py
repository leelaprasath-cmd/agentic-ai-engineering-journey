

print("========== LOOPS IN PYTHON ==========")


print("\n========== FOR LOOP ==========")

for i in range(1, 6):
    print("Day", i)



print("\n========== WHILE LOOP ==========")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


print("\n========== BREAK STATEMENT ==========")

for number in range(1, 11):

    if number == 6:
        print("Loop stopped at", number)
        break

    print(number)



print("\n========== CONTINUE STATEMENT ==========")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)

print("\n========== NESTED LOOPS ==========")

for row in range(1, 4):

    for column in range(1, 4):

        print(row, column)



print("\n========== STAR PATTERN ==========")

for i in range(1, 6):

    for j in range(i):

        print("*", end=" ")

    print()

print("\n========== PROGRAM COMPLETED ==========")
