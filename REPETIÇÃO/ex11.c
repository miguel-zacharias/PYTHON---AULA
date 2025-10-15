//feitoporzacharias
// Exercício 5 em C
#include <stdio.h>
#include <string.h>

int main() {
    char senha[20];
    do {
        printf("Digite a senha: ");
        scanf("%s", senha);
        if(strcmp(senha, "python123") != 0) {
            printf("Senha incorreta! Tente novamente.\n");
        }
    } while(strcmp(senha, "python123") != 0);
    printf("Acesso permitido!\n");
    return 0;
}