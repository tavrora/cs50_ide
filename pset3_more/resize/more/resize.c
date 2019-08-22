// Resizes a BMP file

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: multiplier infile outfile\n");
        return 1;
    }

    float multiplier = atof(argv[1]);

    // coefficient value check
    if (multiplier <= 0.0 || multiplier > 100.0)
    {
        printf("Usage: multiplier infile outfile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        printf("Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        printf("Unsupported file format.\n");
        return 4;
    }

    // вычисляем новую ширину картинки в пикселях
    float flNewWidth = bi.biWidth * multiplier;
    // отбрасываем дробную часть новой ширины и преобразуем в целое
    float floorNewWidth = floor(flNewWidth);
    int intNewWidth = (int)floorNewWidth;
    // высота равна ширине (тут не учитывается знак высоты)
    int intNewHeight = intNewWidth;

    printf("w = %i, h = %i\n", intNewWidth, intNewHeight);

    // the maximum allowable value of the variable of the DWORD type, which stores the image size in bits
    unsigned long int limit = pow(2, 32) - 1;
    // size of the new image in bits
    unsigned long int newSize = (intNewWidth * intNewHeight * sizeof(RGBTRIPLE) + 54) * 8;
    // printf("%lu, %lu\n", limit, newSize); // debug output
    // check for the maximum allowed value (of type dword)
    if (newSize > limit)
    {
        printf("Usage: multiplier infile outfile\n");
        return 1;
    }

    // save original sizes
    int inSizeImage = bi.biSizeImage;
    int inWidth = bi.biWidth;
    int inHeight = bi.biHeight;

    // create variables for structures
    BITMAPFILEHEADER bfh;
    BITMAPINFOHEADER bih;

    bfh = bf;
    bih = bi;

    // determine old padding for scanlines in bytes
    int oldPadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    // determine old padding for scanlines in pixels
    int oldPaddingInPixels = oldPadding / 3;

    // determine new padding for scanlines in bytes
    int padding = (4 - (intNewWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    // determine new padding for scanlines in pixels
    int paddingInPixels = padding / 3;

    // define new size values
    if (multiplier != 1.0)
    {
        bih.biWidth = intNewWidth;
        // сохраняет знак значения высоты
        bih.biHeight = intNewHeight * (bi.biHeight / abs(bi.biHeight));
        bih.biSizeImage = abs(bih.biHeight) * (bih.biWidth * sizeof(RGBTRIPLE) + padding);
        bfh.bfSize = bih.biSizeImage + 54;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bfh, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bih, sizeof(BITMAPINFOHEADER), 1, outptr);

    // округляем множитель и преобразуем в целое
    float flMultiplier = roundf(multiplier);
    int intMultiplier = (int)flMultiplier;
    printf("intMultiplier = %i\n", intMultiplier);

    // ветка для дробного множителя больше единицы (увеличение)
    if (floor(multiplier) != multiplier && multiplier > 1)
    {
        // iterate over infile's scanlines
        for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
        {
            if (i % 2 == 0)
            {
                // iterate over scanlines
                for (int h = 0; h < intMultiplier; h++)
                {
                    // iterate over pixels in scanline
                    for (int j = 0; j < bi.biWidth; j++)
                    {
                        // temporary storage
                        RGBTRIPLE triple;

                        // read RGB triple from infile
                        // (reads a pixel at a time, so there are 3 bytes at a time)
                        fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                        if (j % 2 == 0)
                        {
                            // write RGB triple to outfile
                            for (int w = 0; w < intMultiplier; w++)
                            {
                                fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                            }
                        }
                        else
                        {
                            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                        }

                    }

                    // add zeros for alignment in bytes
                    for (int k = 0; k < padding; k++)
                    {
                        fputc(0x00, outptr);
                    }

                    // move the pointer to the beginning of the line to copy it in height
                    fseek(inptr, -(bi.biWidth * sizeof(RGBTRIPLE)), SEEK_CUR);
                }
            }
            else
            {
                // iterate over pixels in scanline
                for (int j = 0; j < bi.biWidth; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    // (reads a pixel at a time, so there are 3 bytes at a time)
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    if (j % 2 == 0)
                    {
                        // write RGB triple to outfile
                        for (int w = 0; w < intMultiplier; w++)
                        {
                            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                        }
                    }
                    else
                    {
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
                }

                // add zeros for alignment in bytes
                for (int k = 0; k < padding; k++)
                {
                    fputc(0x00, outptr);
                }

                // move the pointer to the beginning of the line to copy it in height
                fseek(inptr, -(bi.biWidth * sizeof(RGBTRIPLE)), SEEK_CUR);
            }

            // return the pointer back
            fseek(inptr, (bi.biWidth * sizeof(RGBTRIPLE) + oldPadding), SEEK_CUR);
        }
    }

    // ветка для дробного множителя меньше единицы (уменьшение) - переписать на уменьшение
    else if (floor(multiplier) != multiplier && multiplier < 1)
    {
        // iterate over infile's scanlines
        for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
        {
            if (i % 2 == 0)
            {
                // iterate over pixels in scanline
                for (int j = 0; j < bi.biWidth; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    // (reads a pixel at a time, so there are 3 bytes at a time)
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    if (j % 2 == 0)
                    {
                        // write RGB triple to outfile
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
                    // else
                    // {
                    //     fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    // }

                }

                // add zeros for alignment in bytes
                for (int k = 0; k < padding; k++)
                {
                    fputc(0x00, outptr);
                }

                // move the pointer to the beginning of the line to copy it in height
                fseek(inptr, -(bi.biWidth * sizeof(RGBTRIPLE)), SEEK_CUR);
            }

            // return the pointer back
            fseek(inptr, (bi.biWidth * sizeof(RGBTRIPLE) + oldPadding), SEEK_CUR);
        }
    }

    // ветка для целочисленного множителя
    else
    {
        // iterate over infile's scanlines
        for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
        {
            for (int h = 0; h < intMultiplier; h++)
            {
                // iterate over pixels in scanline
                for (int j = 0; j < bi.biWidth; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile (читает пиксель за раз, то есть 3 байта за раз)
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    // write RGB triple to outfile
                    for (int w = 0; w < intMultiplier; w++)
                    {
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
                }

                // добавить нули для выравнивания в байтах
                for (int k = 0; k < padding; k++)
                {
                    fputc(0x00, outptr);
                }

                // перемещаем указатель в начало строки для её копирования по высоте
                fseek(inptr, -(bi.biWidth * sizeof(RGBTRIPLE)), SEEK_CUR);
            }

            // возвращаем указатель обратно
            fseek(inptr, (bi.biWidth * sizeof(RGBTRIPLE) + oldPadding), SEEK_CUR);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}