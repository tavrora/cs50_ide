from cs50 import get_string
import sys


def main():

    # проверяем количество аргументов командной строки
    if len(sys.argv) != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)

    # открываем файл и читаем по одной строке с записью ее в качестве элемента списка
    with open(sys.argv[1], 'r') as dictionary:
        dictList = dictionary.readlines()       # теперь у нас есть список из стоп-слов

    # dictionary.close() - конструкция with сама закрывает файл за собой

    # if 'geez\n' in dictList:
    #     print("ololol")

    while True:
        print("What message would you like to censor?")
        userText = get_string("")
        if len(userText) > 0:
            break

    # разбиваем пользовательскую строку на слова по пробелу и сохраняем в списке
    textList = userText.split()

    # превращаем список в набор для более быстрого поиска
    stopWords = set(dictList)
    # testWords = set(textList) # в наборе слова путаются местами!

    # проверяем каждое слово пользователя по словарю
    for i in textList:
        # запикиваем, если найдено
        if i.lower()+'\n' in stopWords:
            print("*" * len(i) + " ", end="")
        # печатаем без изменений, если не найдено
        else:
            print(f"{i} ", end="")

    print()

    sys.exit(0)


if __name__ == "__main__":
    main()
