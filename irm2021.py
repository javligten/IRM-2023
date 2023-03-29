"""Defines the correct and incorrect spelling values"""
correct = "cadeau"
incorrect = "kado"

"""Reads the txt.file and splits the text in words"""
with open('christmas2012.txt', 'r') as f:
    text = f.read()

words = text.strip()

"""Counts the occurences of "kado" and "cadeau" and creates a total value to get the frequency (result)"""
count_incorrect = words.count(incorrect)
count_correct = words.count(correct)
total = words.count(incorrect) + words.count(correct)
result = count_incorrect/total, count_correct/total
difference = count_correct - count_incorrect

"""Prints the comparison of both words in frequency""" 
if count_incorrect > count_correct:
    print(f"'{incorrect}' has a higher usage frequency than '{correct}'", result, "with a difference of:", difference)
elif count_correct > count_incorrect:
    print(f"'{incorrect}' has a lower usage frequency than '{correct}'", result, "with a difference of:", difference)
else:
    print(f"'{incorrect}' and '{correct}' have the exact same usage frequency", result), difference
