#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    char *infile = argv[1];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // определяем размер файла
    // перемещаем указатель в конец
    fseek(inptr, 0, SEEK_END);
    // сохраняем позицию указателя - это и есть размер файла в блоках
    int fileSize = ftell(inptr);
    // определяем размер файла в блоках по 512 байт
    int fileSizeInBlocks = fileSize / 512;
    // возвращаем указатель в начало файла для дальнейшего использования
    rewind(inptr);

    // задаем буфер для хранения прочитанного
    unsigned char buffer[512];
    // создаем указатель на выходной файл
    FILE *outptr;
    // объявляем переменную для имени файла
    char nameJpg[8];
    // часть имени - порядковый номер
    char numberJpg = 0;

    // int a = 0;
    int currentPointer; // текущая позиция указателя

    for (int j = 0; j < fileSizeInBlocks; j++)
    {
        fread(buffer, 512, 1, inptr);
        // проверяем, действительно ли эти байты соответствуют началу jpg-файла
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff
            // && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
            && (buffer[3] == 0xe0 || buffer[3] == 0xe1 || buffer[3] == 0xe2 || buffer[3] == 0xe3 || buffer[3] == 0xe4 || buffer[3] == 0xe5
                || buffer[3] == 0xe6 || buffer[3] == 0xe7 || buffer[3] == 0xe8 || buffer[3] == 0xe9 || buffer[3] == 0xea || buffer[3] == 0xeb
                || buffer[3] == 0xec || buffer[3] == 0xed || buffer[3] == 0xee || buffer[3] == 0xef))
        {
            // готовим имя для файла
            sprintf(nameJpg, "%03d.jpg", numberJpg);
            numberJpg = numberJpg + 1;

            // открываем созданный файл
            outptr = fopen(nameJpg, "w");

            fwrite(buffer, 512, 1, outptr);
            fread(buffer, 512, 1, inptr);

            while (!(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff
                     && (buffer[3] == 0xe0 || buffer[3] == 0xe1 || buffer[3] == 0xe2 || buffer[3] == 0xe3 || buffer[3] == 0xe4 || buffer[3] == 0xe5
                         || buffer[3] == 0xe6 || buffer[3] == 0xe7 || buffer[3] == 0xe8 || buffer[3] == 0xe9 || buffer[3] == 0xea || buffer[3] == 0xeb
                         || buffer[3] == 0xec || buffer[3] == 0xed || buffer[3] == 0xee || buffer[3] == 0xef)))
            {
                // записываем в выходной файл пока не встеретилось начало нового
                fwrite(buffer, 512, 1, outptr);

                // проверка на достижение конца файла - надо не давать читать, если достигнут конец файла
                currentPointer = ftell(inptr);
                if (currentPointer + 512 > fileSize)
                {
                    break;
                }

                // на последней итерации тут в памяти появлется новый незаписанный заголовок (пытается зайти за размер файла 049)
                fread(buffer, 512, 1, inptr);
            }
            fclose(outptr);

            // printf("%i\n", a); // отследить итерацию
            // a = a + 1;

            fseek(inptr, -512, SEEK_CUR);  // ломает при последнем прохождении
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    // fclose(outptr);

    // success
    return 0;
}