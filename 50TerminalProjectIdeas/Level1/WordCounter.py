print("Word Counter")
print("-"*30)

print("User Instructions:")
print("1. Enter the text you want to analyze.")
print("2. The tool will count the number of words in the text.")
print("-"*30)

text = input("Enter your text: ")

word_count = len(text.split())
print(f"The number of words in the text is: {word_count}")
