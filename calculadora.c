#include <stdio.h>

int main() {
    float num1, num2, resultado;
    char operacao;

    // Solicitação de entrada do usuário
    printf("Digite o primeiro número: ");
    scanf("%f", &num1);

    printf("Digite a operação (+, -, *, /): ");
    scanf(" %c", &operacao);  // O espaço antes de %c ignora os espaços em branco

    printf("Digite o segundo número: ");
    scanf("%f", &num2);

    // Realiza a operação escolhida
    switch (operacao) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                resultado = num1 / num2;
            } else {
                printf("Erro: Divisão por zero!\n");
                return 1;  // Termina o programa com código de erro
            }
            break;
        default:
            printf("Operação inválida!\n");
            return 1;  // Termina o programa com código de erro
    }

    // Exibe o resultado
    printf("Resultado: %.2f\n", resultado);

    return 0;  // Termina o programa com sucesso
}

