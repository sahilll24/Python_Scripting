# For success of this code you must have given file in your current directory

with open('current_time.py','r') as f:
    text = f.read()
lines = text.split('\n')
words = text.split()
characters = len(text)

print(f"Number of lines in file :- {len(lines)}")
print(f"Number of words in file :- {len(words)}")
print(f"Number of characters in file :- {characters}")