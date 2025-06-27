def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

def format_phone_number(number: str) -> str:
    """Format a phone number string to (XXX) XXX-XXXX if possible."""
    digits = [c for c in number if c.isdigit()]
    if len(digits) == 10:
        return f"({''.join(digits[:3])}) {''.join(digits[3:6])}-{''.join(digits[6:])}"
    return number