#!/usr/bin/env python3
import sys
import crypt
import string
from cs50 import get_string

# crypt.crypt(word, salt)

# проверяем количество аргументов командной строки
if len(sys.argv) != 2:
    print("Usage: python crack.py hash")
    sys.exit(1)

# salt determination (первые две буквы хэша)
salt = sys.argv[1][0] + sys.argv[1][1]

# string.ascii_letters --> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_lowercase --> 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase --> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(string.ascii_letters[i])

for c in string.ascii_letters:     # enumeration of all 1 letters
    # determine hash
    hash = crypt.crypt(c, salt)

    # check the match
    if hash == sys.argv[1]:
        print(c)
        sys.exit(0)


for c in string.ascii_letters:     # enumeration of all 2 letters
    # loop to iterate over the next letter
    for c1 in string.ascii_letters:

        # склеиваем пароль из букв
        password = c + c1

        # determine hash
        hash = crypt.crypt(password, salt)

        # check the match
        if hash == sys.argv[1]:
            print(password)
            sys.exit(0)


for c in string.ascii_letters:     # enumeration of all 3 letters
    for c1 in string.ascii_letters:
        for c2 in string.ascii_letters:

            password = c + c1 + c2
            hash = crypt.crypt(password, salt)
            if hash == sys.argv[1]:
                print(password)
                sys.exit(0)


for c in string.ascii_letters:     # enumeration of all 4 letters
    for c1 in string.ascii_letters:
        for c2 in string.ascii_letters:
            for c3 in string.ascii_letters:

                password = c + c1 + c2 + c3
                hash = crypt.crypt(password, salt)
                if hash == sys.argv[1]:
                    print(password)
                    sys.exit(0)


for c in string.ascii_letters:     # enumeration of all 5 letters
    for c1 in string.ascii_letters:
        for c2 in string.ascii_letters:
            for c3 in string.ascii_letters:
                for c4 in string.ascii_letters:

                    password = c + c1 + c2 + c3 + c4
                    hash = crypt.crypt(password, salt)
                    if hash == sys.argv[1]:
                        print(password)
                        sys.exit(0)


sys.exit(1)
