from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # a и b - это строки! (а не файлы, которые надо открывать для чтения)
    # создаём списки для хранения всех строк из строк-аргументов без (\n)
    list1 = a.splitlines()
    list2 = b.splitlines()

    # список для хранения строки, если она есть в первой стоке (а) и во второй строке (b)
    listSimilar = [line for line in list1 if line in list2]

    # переводим итоговый список совпадений в набор для удаления дублей (но записи перемешиваются...)
    setSimilar = set(listSimilar)

    return setSimilar


def sentences(a, b):
    """Return sentences in both a and b"""

    list1 = sent_tokenize(a)
    list2 = sent_tokenize(b)

    listSimilar = [sentence for sentence in list1 if sentence in list2]

    setSimilar = set(listSimilar)
    return setSimilar


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    list1 = []
    aLen = len(a)-(n-1)

    for i in range(aLen):
        substr = a[i:(i+n)]
        list1.append(substr)

    list2 = []
    bLen = len(b)-(n-1)

    for i in range(bLen):
        substr = b[i:(i+n)]
        list2.append(substr)

    listSimilar = [substr for substr in list1 if substr in list2]

    setSimilar = set(listSimilar)
    return setSimilar
