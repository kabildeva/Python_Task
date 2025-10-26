text = "I am New to this office but not New to Role"
word = input("Enter word to count: ")
count = text.lower().split().count(word.lower())
print("Number of occurrences:", count)
