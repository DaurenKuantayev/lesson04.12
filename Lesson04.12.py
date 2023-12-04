# try:
#      result = "10" + 5
# except TypeError as e:
#     print(f'TypeError: {e}')

# try:
#     number = int('abc')
# except ValueError as e:
#     print(f'TypeError: {e}')

# class MyClass:
#     pass
#
# try:
#     instance = MyClass()
#     instance.name
#
# except AttributeError as e:
#     print(f'Attribute Error {e}')

# class MyClass:
# #     def __init__(self):
# #         self._name = str
# #
# #
# # instance = MyClass()
# # instance.name

# try:
#     num1 = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#
#     result = num1 / num2
#     print(f'Result: {result}')
#
# except ValueError:
#     print('Вы ввели невалидное значение')
#
# except ZeroDivisionError:
#     print('Делить на ноль запрещено!')

# try:
#     num = input('Enter number: ')
#     num = int(num)
#     print(f'Number {num}')
# except ValueError:
#     print('Invalid digit')

# l = [1, 2, 3, 4]
#
#
# def get_element_by_index(index):
#     try:
#         l[index]
#     except ValueError:
#         print('Value Error')
#     except IndexError:
#         print('Index out of range')
#     else:
#         print(f'everything is okay {l[index]}')
#     finally:
#         return 'You are good anyway'
#
#
# print(get_element_by_index('dffdd'))

# a = input('Enter number: ')
# if a.isdigit():
#     print(f'Congrats {a}')
#
# while not a.isdigit():
#     try:
#         a = int(a)
#         print(f'your number {a}')
#         break
#     except ValueError:
#         a = input('Invalid number, try again: ')
#
#     else:
#         print(f'Congrats {a}')

# class AgeError(ValueError):
#     def __init__(self, age):
#         self.age = age
#         super.__str__(f'Ошибка возраста: {age}. Возраст должен быть от 0 до 150')
#
#
# try:
#     age = int(input('Введите ваш возраст: '))
#
#     if not 0 < age < 150:
#         raise AgeError(str(age))
#
#     print(f'Возраст {age}')
#
# except AgeError as e:
#     print(f'Ошибка: {e}')
#
# except ValueError:
#     print('Введите корректный номер!')

# import re
#
#
# class EmailFormatError(ValueError):
#     def __init__(self, email: str):
#         self.email = email
#
#     def __str__(self):
#         return f'{email}: invalid email'
#
#
# try:
#     email = input('Enter your email: ')
#
#     if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         raise EmailFormatError(email)
#
#     print(f'Your email address is: {email}')
# except EmailFormatError as e:
#     print(e)


class PasswordLengthError(ValueError):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f'Your password is less than 8 characters!'

try:
    password = input('Enter your password: ')
    if len(password) < 8:
        raise PasswordLengthError(password)

    print('Password accepted!')

except PasswordLengthError as e:
    print(f'Error {e}')