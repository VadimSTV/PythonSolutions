#print ("Hello people!")    
#greetings = "it's your daddy"
#for i in range (3) :
#    print("Hi, my little princess! ", greetings)

#x = 10
#if x < 10 :
#    print(x, "меньше 10!")
#elif x > 10 :
#    print(x, "больше 10!")
#elif x == 10:
#    print(x, "равно 10!")

#x1 = 10
#x2 = 25
#x3 = 26
#if x1 <= 10 :
#    print(x1, "<= 10")
#if x2 > 10 and x2 <= 25:
#    print("переменная",x2, " больше 10, но", x2, "переменная меньше или равна 25" )
#if x3 > 25 :
#    print("переменная", x3, "больше 25")

#x = 10
#y = 3
#remainder = x % y
#print(x, "%", y, "остаток",remainder)

# Частное
#a = int(input())
#b = int(input())
#c = a / b
#print(a, "/",b, "Частное", c)

# Четырёхзначное число
#a = int(input())
#print("Цифра в позиции тысяч равна", a // 1000)
#print("Цифра в позиции сотен равна", a % 1000 // 100)
#rint("Цифра в позиции десятков равна", a % 100 // 10)
#print("Цифра в позиции единиц равна", a % 10)

# Чётное или нечётное
#a = int(input())
#print("Число нечетное") if a % 2 else print("Число четное")

# Роскомнадзор
#a = int(input())
#print("Доступ разрешён" if a >= 18 else print("Доступ запрещён"))

# Арифметическая прогрессия
#a1 = int(input())
#a2 = int(input())
#a3 = int(input())
#if a3 - a2 == a2 -a1 :
#    print("YES")
#else :
#    print("NO")

# Ваш профиль
#my_name = str(input("Введите ваше имя: "))
#my_age = int(input("Введите ваш возраст: "))
#my_weight = float(input("Введите ваш рост: "))
#my_hight = float(input("Введите ваш вес: "))

#print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
#print("Ваши личные данные")
#print("Ваше имя: ",{my_name})
#print("Ваш возраст:",{my_age},"лет")
#print("Ваш рост: ",{my_weight},"см")
#print("Ваш вес: ",{my_hight}," кг")

#Напишите функцию, которая принимает число в качестве ввода, возводит его в квадрат и возвращает.
#num = input("Введите число: ")
#num = int(num)

#num = num ** 2
#print("ваше число в квадрате =", num)

#Создайте функцию, которая принимает строку в качестве параметра и возвращает ее.
#def str(x="Возвращаем строку ") :
#    return x 
#print(str())

#Напишите функцию, которая принимает три обязательных и два необязательных параметра.
#def add_it(a, y, b=10, c=5, d=15) :
#    return a + y + b * c / d
#result = add_it(3, 3)
#print(result)

#Напишите программу с двумя функциями. Первая функция должна принимать в качестве параметра целое число и возвращать
#результат деления этого числа на 2. Вторая функция должна принимать в качестве параметра целое число и возвращать 
#результат умножения этого числа на 4. Вызовите первую функцию, сохраните результат в переменной и передайте её
#в качестве параметра во вторую функцию.

#def f(x) :
#   return x // 2
#param = f(20)
#print(param)

#def f2(y) :
#   return y * 4
#result = f2(param)
#print(result)

#Напишите функцию, которая преобразовывает строку в тип данных float и возвращает результат.
#Используйте обработку исключений, чтобы перехватить возможные исключения.
#hight = input("Укажите ваш вес: ")
#float_hight = float(hight)
#print(hight)