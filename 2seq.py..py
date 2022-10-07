import re
user = input(" Введите элементы списка через запятую:")
new_list = re.split("[,!?:/;]", user)
print(new_list)
unique_user = list(set(user))
print(unique_user)




