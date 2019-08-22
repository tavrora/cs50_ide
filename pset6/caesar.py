#!/usr/bin/env python3
import sys
from cs50 import get_int
from cs50 import get_string

# проверяем количество аргументов командной строки
if len(sys.argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)

# проверяем, что все введенные символы являются цифрами
if not sys.argv[1].isdigit():
    print("Usage: python caesar.py k")
    sys.exit(1)

userKey = int(sys.argv[1])

# проверяем, что число не отрициательное
if userKey < 0:
    print("Usage: python caesar.py k")
    sys.exit(1)

# запрашиваем у пользователя фразу для шифрования
userText = get_string("plaintext: ")
while len(userText) == 0:
    userText = get_string("plaintext: ")

print("ciphertext: ", end="")

l = len(userText)

for i in range(l):
    if userText[i].isalpha() and userText[i].isupper():
        alphaNumberText = ord(userText[i]) - 64
        asciiNumberCipher = (alphaNumberText + userKey) % 26 + 64
        print(chr(asciiNumberCipher), end="")
    elif userText[i].isalpha() and userText[i].islower():
        alphaNumberText = ord(userText[i]) - 96
        asciiNumberCipher = (alphaNumberText + userKey) % 26 + 96
        print(chr(asciiNumberCipher), end="")
    else:
        print(userText[i], end="")

print()
sys.exit(0)