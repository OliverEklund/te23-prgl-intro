print("Men hejsan okänd person! Detta är mitt program!")

user_name = input("Vad är dit namn?:")

print(f"Hej {user_name}! Kul att du är här!")

print("jag undrar hur gammal du är? No reason")
User_age = input("Skriv din ålder i år: ")

user_age_converted = int(User_age)
if int(User_age) >= 120:
    print("verkligen?")
else:
    print("okej")