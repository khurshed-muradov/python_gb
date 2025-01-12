# n = 5
# m = "Five"
# print(type(n))
# print(type(m)) Функция type() показывает в терминале тип переменной
# --------------------
# a = 5
# b = 1.23
# c = "hello"
# print(f"{a} - {b} - {c}")
# print(type(a))
# print(type(b))
# print(type(c))
# print(a, b, c, sep=" - ")
# ---------------------------
# print("Введите первую строку:")
# a = input()
# b = input("Введите вторую строку: ")  # Здесь в аргументе функции input() мы ввели текст, который выходит в одной
# # строке и нигде не сохранятеся также как и функция print()
# print(b)
# -----------------------
# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# print("Введите первое число: ")
# a = int(input())
# b = int(input("Введите второе число: "))
# print(a, " + ", b, " = ", a + b)

# a = 4.234234
# b = 3.2344
# print(
#     round(a * b, 4)
# )  # Функция round() задаёт сколько цифр должно остатся после запятой

# iter = 2
# print(iter)
# iter += 3  # iter = iter + 3
# print(iter)
# iter -= 4  # iter = iter - 4
# print(iter)
# iter *= 5  # iter = iter * 5
# print(iter)
# iter /= 5  # iter = iter / 5
# print(iter)
# iter //= 5  # iter = iter // 5
# print(iter)
# iter %= 5  # iter = iter % 5
# print(iter)
# iter **= 5  # iter = iter ** 5
# print(iter)

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = "qwe"
# b = "qwe"
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это же МАША")
# elif username == "Марина":
#     print("Я так ждала Вас, Марина!")
# elif username == "Ильнар":
#     print("Ильнар - топ)")
# else:
#     print("Привет", username + "!")

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)  # 9

# i = 0
# while i < 5:
#     # if i == 3:
#     #   break
#     i = i + 1
# else:
#     print("Пожалуй")
#     print("Хватит")
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:  # если остаток при делении n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2:  # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# r = range(100, 0, -20)
# for i in r:
#     print(i)


# for i in "qwerty":
#     print(i)

# a = "qwerty"
# print(a[0])

# a = "qwerty"
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = "СъЕШЬ еще этих МяГкИх французких булок"
# print(len(text))
# print("еще" in text)
# print(text.lower())
# print(text.upper())
# print(text.replace("еще", "ЕЩЕ"))

# text = "съешь еще этих мягких французких булок"
# print(text[0]) #с
# print(text[1]) #ъ
# print(text[len(text) - 1]) #к
# print(text[-5]) # б
# print(text[:]) # съешь еще этих мягких французких булок
# print(text[:2]) # съ
# print(text[len(text) - 2 :]) #ок
# print(text[2:9]) # ешь еще
# print(text[6:-18]) # еще этих мягких
# print(text[0 : len(text) : 6]) # сеикалк
# print(text[::6]) # сеикалк
# text = text[2:9] + text[-5] + text[:2] #  ...
