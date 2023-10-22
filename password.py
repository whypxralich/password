import random

password_length = int(input("Введите длину пароля: "))

symbols = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

if password_length < 5:
    print("Ваш пароль слишком короткий и может быть ненадежен. Введите более длинный пароль.")
else:
    password = "".join(random.sample(symbols, password_length))
    print("Ваш пароль:", password)