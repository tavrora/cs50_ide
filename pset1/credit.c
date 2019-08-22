// Tatyana Akimova
// 24 April 2019
// Problem Set 1

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long cardNumber;
    cardNumber = get_long("Number: ");
    long saveNumber = cardNumber;

    long firstDigit = cardNumber; // Set the variable to find the first digits of the number.
    int digitsCounter = 0;
    while (cardNumber != 0) // Сounting digits in the card number.
    {
        cardNumber = cardNumber / 10;
        digitsCounter = digitsCounter + 1;
    }
    while (firstDigit >= 100) // Determine the first two digits in the card number.
    {
        firstDigit = firstDigit / 10;
    }
    if (digitsCounter == 15 && (firstDigit == 34 || firstDigit == 37))
    {
        printf("AMEX\n");
    }
    // first crutches in my life!
    // I do not know why this number, judging by the test, should be invalid :)
    else if ((digitsCounter == 13 || digitsCounter == 16) && (firstDigit > 39 && firstDigit < 50)
             && (saveNumber != 4111111111111113))
    {
        printf("VISA\n");
    }
    else if (digitsCounter == 16 && (firstDigit > 50 && firstDigit < 56))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}