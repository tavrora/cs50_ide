// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
// структура вообще не хранит буквы, только указатели на НИЖЕЛЕЖАЩИЕ индексы
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

// прототип функции рекурсивного освобождения памяти (принимает указатель на узел)
bool recursiveUnload(node *pointerUnload);

unsigned int indexLetter(const char c)
{
    int indexCh;
    // определяем индекс буквы в алфавите (для использования детей)
    if (c != 39) // проверка на апостроф != '\''
    {
        indexCh = tolower(c) - 'a';
    }
    else
    {
        indexCh = 26; // выделяем апострофу последний доступный индекс
    }
    return indexCh;
}

// Represents a trie
node *root = NULL;

// node *newNode; // удалить если не нужен

// счетчик слов
unsigned int coutnWord = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return false;
    }
    root->is_word = false;

    // если убрать эту инициализацию, то количестство ошибок увеличивается на 27! :)))
    // valrgind - ERROR SUMMARY: 9912908
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];
    // длина слова
    int wordLenDict;
    // индекс буквы
    int indexChild;

    node *pointer = root; // устанавливаем узел-указатель на корень дерева

    // работаем побуквенно
    for (int c = fgetc(file); c != EOF; c = fgetc(file))
    {
        // проверка на конец слова
        if (c == '\n')
        {
            pointer->is_word = true;
            coutnWord++;
            pointer = root; // возвращаем узел-указатель на корень дерева
        }
        else
        {
            // определяем индекс буквы в алфавите (для использования детей)
            indexChild = indexLetter(c);

            // если узел по этому индексу еще не создан, то создаем его
            if (pointer->children[indexChild] == NULL)
            {
                // выделяем место новому узлу
                pointer->children[indexChild] = malloc(sizeof(node));
                // проверяем, есть ли это место
                if (pointer->children[indexChild] == NULL)
                {
                    unload();
                    return false;
                }

                // node *tmp = pointer->children[indexChild];

                // если место есть, то дальше инициализируем дочерние узлы
                for (int i = 0; i < N; i++)
                {
                    // tmp->children[i] = NULL;
                    pointer->children[indexChild]->children[i] = NULL;
                }
                // НЕ ХВАТАЛО ИНИЦИАЛИЗАЦИИ IS_WORD
                pointer->children[indexChild]->is_word = false;
            }

            // переход к следующему узлу: смещаем узел-указатель с корня дерева на текущий дочерний элемент
            pointer = pointer->children[indexChild];
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return coutnWord;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // int wordLenText = strlen(word);
    int indexChild;

    node *pointerCheck = root;

    // ИСПРАВИЛА УСЛОВИЕ (int i = 0; i <= wordLenText; i++)
    for (int i = 0; word[i] != '\0'; i++)
    {
        // определяем индекс буквы в алфавите (для использования детей)
        indexChild = indexLetter(word[i]);

        // проверяем по индексу существование узла для каждой буквы
        if (pointerCheck->children[indexChild] == NULL)
        {
            return false;
        }

        // если не NULL, то перемещаем указатель на следующий узел
        pointerCheck = pointerCheck->children[indexChild];
    }

    // после того как мы убдеимся, что существуют узлы для каждой буквы слова -
    // проверям наличие метки окончания слова в текущем указателе
    // if (pointerCheck->is_word == true)      // в этой стороке обращение к неинициализированным значениям
    // {
    //     return true;
    // }
    // return false;

    // или просто возвращаем значение, соответствующее значениию конца слова
    return pointerCheck->is_word;   // в этой стороке было обращение к неинициализированным значениям
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    recursiveUnload(root);
    return true;
}

// функция для рекурсивного освобождения
bool recursiveUnload(node *pointerUnload)
{
    // цикл по всем детям
    for (int i = 0; i < N; i++)
    {
        // проверяем наличие следующего узла
        if (pointerUnload->children[i] != NULL)
        {
            // если узел есть, делаем рекурсивный вызов освобождения
            recursiveUnload(pointerUnload->children[i]);
        }
    }

    // если весь цикл for вернул нули, то освобождаем первый узел, поступивший на вход
    free(pointerUnload);

    return true;
}