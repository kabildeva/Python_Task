s = "kabilan"

# Remove digits first
letters = [i for i in s if not i.isdigit()]
word = "".join(letters)

# Capitalize first and last letter
if len(word) > 1:
    word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
else:
    word = word.upper()

print(word)
