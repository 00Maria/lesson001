name = input('Введите Ваше имя ')
age = int(input('Введите Ваш возраст '))
x = int(input('Введите любое число '))
y = age + x
print( str('Привет, ') + str(name) + str('! Через ') + str(x) + str(' лет Вам будет ') + str(y))
print( 'Привет, {0}! Через {1} лет Вам будет {2}.'.format(name, x, y))

