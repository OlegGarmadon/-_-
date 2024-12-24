def greet_user():
	"""выводит простое приветствие."""
	print("Hello!")

greet_user()

# Передача информации функции.

def greet_user(имя_пользователя):
	print(f"Привет, {имя_пользователя.title()}!")

greet_user('Олег')
greet_user('gregor')

# Аргументы и параметры!

# переменная имя_пользователя в определении  greet_user- это параметр тоесть условные данные необходимые 
# для выполнения ее работы.
# Значение Олег в greet_user -- Это АРГУМЕНТ. Тоесть конкретная информация переданная при вызове функции.

def get_formatted_name(first_name, last_name):
	"""Возвращает акуратно отформатированное полное имя"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#Бесконечный цикл.
while True:
	print("\nPlease tell me your name:")
	f_name = input("first_name")
	l_name = input("last_name")
formated_name = get_formatted_name(f_name, last_name)
print(f"\nHello, {formated_name}!")

"""программа с возможностью выхода"""

def get_formatted_name(first_name, last_name):
	"""Возвращает акуратно отформатированное полное имя"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#Бесконечный цикл.
while True:
	print("\nPlease tell me your name:")

	print("(enter 'q' at any time to quit)")# дороботка выхода из бесконечного цикла.

	f_name = input("first_name")
	if f_name =='q':
		break

	l_name = input("last_name")
	if l_name == 'q':
		break
		
formated_name = get_formatted_name(f_name, last_name)
print(f"\nHello, {formated_name}!")