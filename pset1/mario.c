#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;

    // height entry request
    h = get_int("Height: ");

    //input validation check
    while (h < 1 || h > 8)
    {
        h = get_int("Height: ");
    }

    // building a pyramid
    for (int i = 1; i < h + 1; i++)
    {
        // loop for spaces
        for (int x = 1; x <= h - i; x++)
        {
            printf(" ");
        }
        // cycle for grids
        for (int y = 1; y <= i; y++)
        {
            printf("#");
        }
        printf("\n");
    }
}