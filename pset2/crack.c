#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <crypt.h>

char shift(int i);

int main(int argc, string argv[])
{
    // input validation check
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    // salt determination
    char salt[3] = { argv[1][0], argv[1][1], 0 };
    int asciiNumber;
    string hash;

    // create an array with a set of all valid letters
    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (int j = 0; j <= 25; j++) //enumerate all lowercase letters
    {
        // determine the appropriate letter number
        asciiNumber = 97 + j;

        // translate a character into a numeric value
        char password[3] = {shift(asciiNumber), 0, 0};

        // determine hash
        hash = crypt(password, salt);

        // check the match
        if (strcmp(hash, argv[1]) == 0)
        {
            printf("%s\n", password);
            return 0;
        }
    }

    for (int i = 0; i <= 25; i++) // enumeration of all capital letters
    {
        asciiNumber = 65 + i;
        char password[3] = {shift(asciiNumber), 0, 0};
        hash = crypt(password, salt);

        // check the match
        if (strcmp(hash, argv[1]) == 0)
        {
            printf("%s\n", password);
            return 0;
        }
    }

    for (int i = 0; i <= 51; i++)  // enumeration of all 2 letters
    {
        // loop to iterate over the next letter
        for (int i1 = 0; i1 <= 51; i1++)
        {
            int asciiNumber0 = alphabet[i];
            int asciiNumber1 = alphabet[i1];
            char pass0[3] = {shift(asciiNumber0), 0, 0};
            char pass1[3] = {shift(asciiNumber1), 0, 0};
            string password = strncat(pass0, pass1, 1);
            hash = crypt(password, salt);

            // check the match
            if (strcmp(hash, argv[1]) == 0)
            {
                printf("%s\n", password);
                return 0;
            }
        }
    }

    for (int i = 0; i <= 51; i++)  // enumeration of all 3 letters
    {
        // loop to iterate over the next letter
        for (int i1 = 0; i1 <= 51; i1++)
        {
            // loop to iterate over the next letter
            for (int i2 = 0; i2 <= 51; i2++)
            {
                int asciiNumber0 = alphabet[i];
                int asciiNumber1 = alphabet[i1];
                int asciiNumber2 = alphabet[i2];
                char pass0[3] = {shift(asciiNumber0), 0, 0};
                char pass1[3] = {shift(asciiNumber1), 0, 0};
                char pass2[3] = {shift(asciiNumber2), 0, 0};
                string password0 = strncat(pass0, pass1, 1);
                string password = strncat(password0, pass2, 1);
                hash = crypt(password, salt);

                // check the match
                if (strcmp(hash, argv[1]) == 0)
                {
                    printf("%s\n", password);
                    return 0;
                }
            }
        }
    }

    for (int i = 0; i <= 51; i++)  // enumeration of all 4 letters
    {
        // loop to iterate over the next letter
        for (int i1 = 0; i1 <= 51; i1++)
        {
            // loop to iterate over the next letter
            for (int i2 = 0; i2 <= 51; i2++)
            {
                // loop to iterate over the next letter
                for (int i3 = 0; i3 <= 51; i3++)
                {
                    int asciiNumber0 = alphabet[i];
                    int asciiNumber1 = alphabet[i1];
                    int asciiNumber2 = alphabet[i2];
                    int asciiNumber3 = alphabet[i3];
                    char pass0[3] = {shift(asciiNumber0), 0, 0};
                    char pass1[3] = {shift(asciiNumber1), 0, 0};
                    char pass2[3] = {shift(asciiNumber2), 0, 0};
                    char pass3[3] = {shift(asciiNumber3), 0, 0};
                    string password0 = strncat(pass0, pass1, 1);
                    string password1 = strncat(password0, pass2, 1);
                    string password = strncat(password1, pass3, 1);
                    hash = crypt(password, salt);

                    // check the match
                    if (strcmp(hash, argv[1]) == 0)
                    {
                        printf("%s\n", password);
                        return 0;
                    }
                }
            }
        }
    }

    for (int i = 0; i <= 51; i++)  // enumeration of all 5 letters
    {
        // loop to iterate over the next letter
        for (int i1 = 0; i1 <= 51; i1++)
        {
            // loop to iterate over the next letter
            for (int i2 = 0; i2 <= 51; i2++)
            {
                // loop to iterate over the next letter
                for (int i3 = 0; i3 <= 51; i3++)
                {
                    // loop to iterate over the next letter
                    for (int i4 = 0; i4 <= 51; i4++)
                    {
                        int asciiNumber0 = alphabet[i];
                        int asciiNumber1 = alphabet[i1];
                        int asciiNumber2 = alphabet[i2];
                        int asciiNumber3 = alphabet[i3];
                        int asciiNumber4 = alphabet[i4];
                        char pass0[3] = {shift(asciiNumber0), 0, 0};
                        char pass1[3] = {shift(asciiNumber1), 0, 0};
                        char pass2[3] = {shift(asciiNumber2), 0, 0};
                        char pass3[3] = {shift(asciiNumber3), 0, 0};
                        char pass4[3] = {shift(asciiNumber4), 0, 0};
                        string password0 = strncat(pass0, pass1, 1);
                        string password1 = strncat(password0, pass2, 1);
                        string password2 = strncat(password1, pass3, 1);
                        string password = strncat(password2, pass4, 1);
                        hash = crypt(password, salt);

                        // check the match
                        if (strcmp(hash, argv[1]) == 0)
                        {
                            printf("%s\n", password);
                            return 0;
                        }
                    }
                }
            }
        }
    }

    return 1;
}

// converts a letter to its numeric value
char shift(int i)
{
    return (char) i;
}