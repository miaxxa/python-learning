name = input("your name: ")
year = int(input("your year: "))
age = (2026 - year)
age100 = (year + 100)
if age<12:
    print(f"Hi {name}! You {age} old, in {age100} you age become 100! And you kid. Cool!")
elif age<18:
    print(f"Hi {name}! You {age} old, in {age100} you age become 100! And you teenager. Not bad.")
else:
    print(f"Hi {name}! You {age} old, in {age100} you age become 100! And you adult. Awesome!")