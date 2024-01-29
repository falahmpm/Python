import random
import string

print("Welcome to the Password Generator!!\n")
print("--------------------------------------\n")

letters_count=int(input("How many letters would you like in your password?\n"))
symbols_count=int(input("How many symbols would you like in your password?\n"))
numbers_count=int(input("How many numbers would you like in your password?\n"))



letters_list=list(string.ascii_letters)
symbols_list = list(string.punctuation)
numbers_list=list(range(10))

selected_letters=[]
selected_symbols=[]
selected_numbers=[]


for i in range(letters_count):
    select_number=random.choice(letters_list)
    selected_letters.append(select_number)


print(selected_letters)

for i in range(symbols_count):
    select_number=random.choice(symbols_list)
    selected_symbols.append(select_number)


print(selected_symbols)

for i in range(numbers_count):
    select_number=random.choice(numbers_list)
    selected_numbers.append(str(select_number))


print(selected_numbers)


password_list=selected_letters+selected_symbols+selected_numbers


random.shuffle(password_list)

print(password_list)

password="".join(password_list)


print(f"\n The password generated is :{password}")











