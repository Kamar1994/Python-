SECONDS_IN_MINUTE = 60

second = int(input('Введите количество секунд - '))

minutes = second // SECONDS_IN_MINUTE
second -= minutes * SECONDS_IN_MINUTE

print(minutes, 'минут', second, 'секунд')
