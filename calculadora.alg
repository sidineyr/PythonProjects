BEGIN
    REAL PROCEDURE Adicao(a, b);
        Adicao := a + b
    END Adicao;

    REAL PROCEDURE Subtracao(a, b);
        Subtracao := a - b
    END Subtracao;

    REAL PROCEDURE Multiplicacao(a, b);
        Multiplicacao := a * b
    END Multiplicacao;

    REAL PROCEDURE Divisao(a, b);
        IF b = 0 THEN
            BEGIN
                PRINT("Erro: Divisão por zero!");
                EXIT
            END
        ELSE
            Divisao := a / b
        FI
    END Divisao;

    REAL a, b, resultado;
    CHAR operacao;

    PRINT("Digite o primeiro número: ");
    READ(a);

    PRINT("Digite a operação (+, -, *, /): ");
    READ(operacao);

    PRINT("Digite o segundo número: ");
    READ(b);

    CASE operacao OF
        "+": resultado := Adicao(a, b);
        "-": resultado := Subtracao(a, b);
        "*": resultado := Multiplicacao(a, b);
        "/": resultado := Divisao(a, b);
        OTHERWISE PRINT("Operação inválida!")
    ESAC;

    PRINT("Resultado: ", resultado);

END.

