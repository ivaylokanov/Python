banned_words = input().split()
text = input()
replaced_text = text
for word in banned_words:
    replaced_text = replaced_text.replace(word, "*" * len(word))
print(replaced_text)
