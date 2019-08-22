#!/usr/bin/env python3
import sys
from cs50 import get_string

# функция для преобразования символа в порядковый номер


def shift(c):
    if c.isupper():
        letter = ord(c) - 65
    else:
        letter = ord(c) - 97
    return letter


# проверяем количество аргументов командной строки
if len(sys.argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)

# проверяем, что все введенные символы являются буквами
if not sys.argv[1].isalpha():
    print("Usage: python caesar.py k")
    sys.exit(1)

userKey = sys.argv[1]

# запрашиваем у пользователя фразу для шифрования
userText = get_string("plaintext: ")
while len(userText) == 0:
    userText = get_string("plaintext: ")

print("ciphertext: ", end="")

l = len(userText)
# переменная для прохода по ключу
j = 0

# цикл для каждой буквы введенного текста

for i in range(l):
    if j == len(userKey):
        j = 0
    # шифруем буквы в зависимости от регистра
    if userText[i].isalpha() and userText[i].isupper():
        key = shift(userKey[j])
        alphaNumberText = ord(userText[i]) - 65
        asciiNumberCipher = (alphaNumberText + key) % 26 + 65
        print(chr(asciiNumberCipher), end="")
        j += 1
    elif userText[i].isalpha() and userText[i].islower():
        key = shift(userKey[j])
        alphaNumberText = ord(userText[i]) - 97
        asciiNumberCipher = (alphaNumberText + key) % 26 + 97
        print(chr(asciiNumberCipher), end="")
        j += 1
    else:
        print(userText[i], end="")

print()
sys.exit(0)