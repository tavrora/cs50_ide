#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int shift(char c);

int main(int argc, string argv[])
{
    string userKey;
    if (argc == 2)
    {
        for (int j = 0, n = strlen(argv[1]); j < n; j++)
        {
            if (!isalpha(argv[1][j]))
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
            userKey = argv[1];
        }
    }
    else
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }

    string userText = get_string("plaintext: ");
    while (strlen(userText) == 0)
    {
        userText = get_string("plaintext: ");
    }

    printf("ciphertext: ");
    for (int i = 0, j = 0, n = strlen(userText); i < n; i++, j++) // Text encryption
    {
        if (j == strlen(userKey))
        {
            j = 0;
        }

        if ((isalpha(userText[i])) && (isupper(userText[i])))
        {
            int key = shift(userKey[j]);
            int alphaNumberText = userText[i] - 65;
            int asciiNumberCipher = (alphaNumberText + key) % 26 + 65;
            printf("%c", asciiNumberCipher);
        }
        else if ((isalpha(userText[i])) && (islower(userText[i])))
        {
            int key = shift(userKey[j]);
            int alphaNumberText = userText[i] - 97;
            int asciiNumberCipher = (alphaNumberText + key) % 26 + 97;
            printf("%c", asciiNumberCipher);
        }
        else
        {
            printf("%c", userText[i]);
            j = j - 1;
        }
    }

    printf("\n");
    return 0;
}

int shift(char c) // single character conversion to sequence number
{
    int letter;
    if (isupper(c))
    {
        letter = c - 65;
    }
    else
    {
        letter = c - 97;
    }
    return letter;
}