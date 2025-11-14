#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    if (argc < 4) {
        return 1;
    }

    float n1 = atof(argv[1]);
    float n2 = atof(argv[2]);
    float n3 = atof(argv[3]);

    float media = (n1 + n2 + n3) / 3;

    printf("%.2f", media);

    return 0;
}