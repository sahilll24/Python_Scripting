text = input("Enter the String :-")

vowel = consonant = digit = spaces = 0

vowel_set ='aeiouAEIOU'

for char in vowel_set:
    if char in text:
        vowel +=1
    elif char.isalpha():
        consonant +=1
    elif char.isdigit():
        digit +=1
    elif char.isspace():
        spaces +=1

print(f" vowels :{vowel} , consonant : {consonant} , digit : {digit} , spaces : {spaces}")