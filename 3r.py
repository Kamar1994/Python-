user_number = int(input('Введите число от 0 до 20 - '))

if user_number // 10 == 1 or user_number % 10 > 4 or user_number % 10 == 0:
    end_word = 'ов'

elif user_number % 10 == 1:
    end_word = ''

else:
    end_word = 'а'

print(user_number, 'процент' + end_word)
user_number += 1