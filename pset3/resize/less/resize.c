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

    int multiplier = atoi(argv[1]);

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

    // the maximum allowable value of the variable of the DWORD type, which stores the image size in bits
    unsigned long int limit = pow(2, 32) - 1;
    // size of the new image in bits
    unsigned long int newSize =
        (((bi.biWidth * multiplier) * (abs(bi.biHeight) * multiplier)) * sizeof(RGBTRIPLE) + 54) * 8;
    printf("%lu, %lu\n", limit, newSize);
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
    int padding = (4 - (bi.biWidth * multiplier * sizeof(RGBTRIPLE)) % 4) % 4;
    // determine new padding for scanlines in pixels
    int paddingInPixels = padding / 3;

    // define new size values
    if (multiplier != 1)
    {
        bih.biWidth = bi.biWidth * multiplier;
        bih.biHeight = bi.biHeight * multiplier;
        bih.biSizeImage = abs(bih.biHeight) * (bih.biWidth * sizeof(RGBTRIPLE) + padding);
        bfh.bfSize = bih.biSizeImage + 54;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bfh, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bih, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // iterate over scanlines
        for (int h = 0; h < multiplier; h++)
        {
            // iterate over pixels in scanline
            for (int j = 0; j < bi.biWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                // (reads a pixel at a time, so there are 3 bytes at a time)
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // write RGB triple to outfile
                for (int w = 0; w < multiplier; w++)
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

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}