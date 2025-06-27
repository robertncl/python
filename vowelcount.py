print("\n### Vowel counter ###\n")
string = input("Enter a string: ").lower()
vowels = ["a", "e", "i", "o", "u"]

vowelscounter = 0

def checkVowels(letter):
    for i in range(len(vowels)):
        if letter == vowels[i]:
            return True
    return False

for i in range(len(string)):
    if checkVowels(string[i]):
        vowelscounter = vowelscounter + 1

print(f"\n### {vowelscounter} vowel(s) were found in the string. ###")

def vowel_count(text: str) -> int:
    """Return the number of vowels in the input text."""
    return sum(1 for c in text.lower() if c in 'aeiou')