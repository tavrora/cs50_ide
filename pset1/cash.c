#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float changeFl;
    changeFl = get_float("Change owed: ");
    printf("changeFl = %f\n", changeFl);
    while (changeFl <= 0)
    {
        changeFl = get_float("Change owed: ");
    }
    float centFl = changeFl * 100;
    printf("centFl = %f\n", centFl);

    // change in cents
    // round to avoid inaccuracies
    int centInt = round(centFl);

    printf("centInt = %i\n", centInt);

    // coin counter
    int coinСounter = 0;

    // I don't understand why I need to add 1
    int remainder = centInt;
    printf("all remainder = %i, coinСounter = %i\n", remainder, coinСounter);

    while (remainder >= 25)
    {
        remainder = remainder - 25;
        coinСounter = coinСounter + 1;
        printf("25 remainder = %i, coinСounter = %i\n", remainder, coinСounter);
    }
    while (remainder < 25 && remainder >= 10)
    {
        remainder = remainder - 10;
        coinСounter = coinСounter + 1;
        printf("10 remainder = %i, coinСounter = %i\n", remainder, coinСounter);
    }
    while (remainder < 10 && remainder >= 5)
    {
        remainder = remainder - 5;
        coinСounter = coinСounter + 1;
        printf("5 remainder = %i, coinСounter = %i\n", remainder, coinСounter);
    }
    while (remainder < 5 && remainder >= 1)
    {
        remainder = remainder - 1;
        coinСounter = coinСounter + 1;
        printf("1 remainder = %i, coinСounter = %i\n", remainder, coinСounter);
    }
    printf("%i\n", coinСounter);
}