m = float(input('Введите целое положительное число '))
if m < 0:
    print('Вы ввели отрицательное число')
elif m % 1 > 0:
    print('Вы ввели дробное число')
elif m > 0 and m % 1 == 0:
    max = m % 10
    while m >= 1:
        m = m // 10
        if m % 10 > max:
            max = m % 10
        if m > 9:
            continue
        else:
            print('Максимальное цифра в числе ', max)
            break
