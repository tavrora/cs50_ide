// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table устанавливается указаетель на хеш-таблицу
node *hashtable[N];
// инициализируем новый узел
node *newNode = NULL;  // для доступа из load и unload

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
// Функция хэша возвращает индекс по первой букве слова
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// заводим переменную для счетчика слов
unsigned int count = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char wordBuffer[LENGTH + 1];

    // Insert words into hash table
    // считывает из file строку символов до пробела (?) и кладёт это в wordBuffer, пока не достигнет конца файла
    while (fscanf(file, "%s", wordBuffer) != EOF)
    {
        // добавляет символ окончания слова в конец слова
        wordBuffer[strlen(wordBuffer)] = '\0';
        // выделяем место для этого нового узла
        newNode = malloc(sizeof(node));
        // проверяем, есть ли это место
        if (newNode == NULL)
        {
            unload();
            return false;
        }

        // копируем слово в новый узел из wordBuffer
        strcpy(newNode -> word, wordBuffer);

        // хэшируем слово, помещенное в узел, чтобы определить корзину узла
        unsigned int indexWord = hash(wordBuffer);
        // добавляем новый узел в начало списка, сдвигая весь остальной
        newNode -> next = hashtable[indexWord]; // новый узел указывает туда же, куда и голова
        hashtable[indexWord] = newNode; // голова указвает на новый узел

        // увеличиваем счетчик слов в словаре
        count ++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int numberWords = count;
    return numberWords;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // создаем новый указатель для поиска и говорим ему указывать туда же, куда и голова - на первый элемент (устанавливаем его на "голову-head" НУЖНОЙ корзины.)
    node *cursor = hashtable[hash(word)];

    while (cursor != NULL) // конец цепочки
    {
        // если при сравнении слов без учета регистра условие равно 0 - значит слово текста совпало со свловом из словаря!
        if (strcasecmp(cursor -> word, word) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }

    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // проходим циколом через все корзины
    for (int i = 0; i < N; i++)
    {
        // проходим через каждый узел в корзине и освобождаем его
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
    }

    return true;
}