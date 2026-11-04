import random


def create_password_generator(characters):
    def create_password(length):
        return ''.join(random.choice(characters) for _ in range(length))
    return create_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))
