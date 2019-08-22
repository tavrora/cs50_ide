#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    h = get_int("Height: ");
    while (h < 1 || h > 8)
    {
        h = get_int("Height: ");
    }

    for (int i = 1; i < h + 1; i++)
    {
        for (int x = 1; x <= h - i; x++)
        {
            printf(" ");
        }
        for (int y = 1; y <= i; y++)
        {
            printf("#");
        }
        printf("  ");
        for (int y = 1; y <= i; y++)
        {
            printf("#");
        }
        printf("\n");
    }
}
