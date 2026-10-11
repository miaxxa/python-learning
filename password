import secrets
import string
length = (int(input("Введите длину пароля: ")))
chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(secrets.choice(chars) for _ in range(length))
print("Пароль:", password)