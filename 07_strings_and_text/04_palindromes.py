text = input()
words = text.split( )
palindromes = [word for word in words if word == word[::-1]]
palindromes = set(palindromes)
print(', '.join(sorted(palindromes, key=str.lower)))