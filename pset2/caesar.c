// Tatyana Akimova
// 24 April 2019
// Problem Set 2

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    int userKey;
    if (argc != 2)
    {
        return 1;
    }

    for (int j = 0, n = strlen(argv[1]); j < n; j++) // Сheck that the user input only numbers
    {
        if (!isdigit(argv[1][j]))
        {
            printf("Usage: %c.", argv[1][j]);
            return 1;
        }
    }

    userKey = atoi(argv[1]); // Convert strings to integer
    if (userKey < 0)
    {
        return 1;
    }

    string userText = get_string("plaintext: ");
    while (strlen(userText) == 0)
    {
        userText = get_string("plaintext: ");
    }

    printf("ciphertext: ");
    for (int i = 0, n = strlen(userText); i < n; i++) // Text encryption
    {
        if ((isalpha(userText[i])) && (isupper(userText[i])))
        {
            int alphaNumberText = userText[i] - 64;
            int asciiNumberCipher = (alphaNumberText + userKey) % 26 + 64;
            printf("%c", asciiNumberCipher);
        }
        else if ((isalpha(userText[i])) && (islower(userText[i])))
        {
            int alphaNumberText = userText[i] - 96;
            int asciiNumberCipher = (alphaNumberText + userKey) % 26 + 96;
            printf("%c", asciiNumberCipher);
        }
        else
        {
            printf("%c", userText[i]);
        }
    }

    printf("\n");
    return 0;
}