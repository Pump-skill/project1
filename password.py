a=input('Введите пароль: ')
 

try:
    c = 10 / len(a)
    d=int(a)
    print('Ваш пароль состоит только из цифр')


except ZeroDivisionError:
    print('Вы ввели пустой пароль')

except ValueError: 
    print('Требования к паролю соблюденыe')   