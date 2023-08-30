'''Задача3: - по желанию
Напишите программу, которая запрашивает у пользователя три числа и выполняет следующие проверки:

Если первое число больше 100, выбросить исключение NumberOutOfRangeException с сообщением
"Первое число вне допустимого диапазона".
Если второе число меньше 0, выбросить исключение NumberOutOfRangeException с сообщением
"Второе число вне допустимого диапазона".
Если сумма первого и второго чисел меньше 10, выбросить исключение NumberSumException с сообщением
"Сумма первого и второго чисел слишком мала".
Если третье число равно 0, выбросить исключение DivisionByZeroException с сообщением
"Деление на ноль недопустимо".
В противном случае, программа должна выводить сообщение "Проверка пройдена успешно".
- необходимо создать 3 класса собвстенных исключений'''

class NumberOutOfRangeException(Exception):
    pass

class NumberSumException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

def  nums_correct(num_1: int, num_2: int, num_3: int) -> str:
    try:
        if num_1 > 100:
            raise NumberOutOfRangeException('Первое число вне допустимого диапазона')
        if num_2 < 0:
            raise NumberOutOfRangeException('Второе число вне допустимого диапазона')
        if num_1 + num_2 < 10:
            raise NumberSumException('Сумма первого и второго чисел слишком мала')
        if num_3 == 0:
            raise DivisionByZeroException('Деление на ноль недопустимо')
        return 'Проверка пройдена успешно'
    except NumberOutOfRangeException as err:
        return err
    except NumberSumException as err:
        return err
    except DivisionByZeroException as err:
        return err

print(nums_correct(int(input('Введите 1-е число: ')), int(input('Введите 2-е число: ')), int(input('Введите 3-е число: '))))