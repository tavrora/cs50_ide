from cs50 import get_int

cardNumber = get_int("Number: ")
strNumber = str(cardNumber)

sumMultiDigits = 0      # переменная для суммы умноженных на 2 чисел
l = len(strNumber) - 1      # длина номера (-1 для индексации)

for i in range(l + 1):      # для всех i в длине номера
    if i % 2 != 0:      # если i нечетное
        if int(strNumber[l-i]) * 2 < 10:      # умножаем на 2 все цифры в номере карты, начиная с предпоследней
            sumMultiDigits = sumMultiDigits + int(strNumber[l-i]) * 2      # суммируем однозначные произведения
        else:      # если результат умножения на 2 получился двузначным: strNumber[l-i] * 2 >= 10
            subNumber = str(int(strNumber[l-i]) * 2)        # умножаем целые и переводим результат обратно в строку
            # находим сумму цифр в двузначном произведении и прибавляем ее к основной сумме
            sumMultiDigits = sumMultiDigits + int(subNumber[0]) + int(subNumber[1])

sumSingleDigits = 0    # переменная для суммы чисел, которые не были умножены на 2

for i in range(l + 1):
    if i % 2 == 0:
        if int(strNumber[l-i]) < 10:
            sumSingleDigits = sumSingleDigits + int(strNumber[l-i])
        else:
            subNumber = str(strNumber[l-i])
            sumSingleDigits = sumSingleDigits + int(subNumber[0]) + int(subNumber[1])

sumTotal = sumMultiDigits + sumSingleDigits

if sumTotal % 10 != 0:     # если последняя цифра в сумме не 0, то карта не валидная
    print("INVALID")
else:
    # print("GOOD!")
    firstDigits = cardNumber
    while firstDigits >= 100:
        firstDigits = firstDigits // 10       # определяем первые две цифры номера карты

    # провекра соответствия карты
    if len(strNumber) == 15 and (firstDigits == 34 or firstDigits == 37):
        print("AMEX")
    elif (len(strNumber) == 13 or len(strNumber) == 16) and (firstDigits > 39 and firstDigits < 50):
        print("VISA")
    elif len(strNumber) == 16 and (firstDigits > 50 or firstDigits < 56):
        print("MASTERCARD")
    else:
        print("INVALID")
