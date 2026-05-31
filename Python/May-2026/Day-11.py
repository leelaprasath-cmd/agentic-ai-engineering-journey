# ==========================================
# DAY 11 — STRING METHODS PRACTICE
# ==========================================

print("===== STRING METHODS PRACTICE =====")

sentence = input("Enter a sentence: ")

print("\nOriginal :", sentence)

print("Upper Case :", sentence.upper())

print("Lower Case :", sentence.lower())

print("Title Case :", sentence.title())

print("Word Count :", len(sentence.split()))

search_word = input("\nEnter a word to search: ")

if search_word.lower() in sentence.lower():

    print("Word Found")

else:

    print("Word Not Found")

print("\n===== PROGRAM COMPLETED =====")
