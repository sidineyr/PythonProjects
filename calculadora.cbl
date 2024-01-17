       IDENTIFICATION DIVISION.
       PROGRAM-ID. Calculadora.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 Num1 PIC 9(5) VALUE 0.
       01 Num2 PIC 9(5) VALUE 0.
       01 Result PIC 9(10) VALUE 0.
       01 Operacao PIC X VALUE ' '.
       01 Mensagem PIC X(100) VALUE SPACES.

       SCREEN SECTION.
       01 Tela.
          02 Linha-1.
             03 Col-1   PIC X(100) VALUE SPACES.
          02 Linha-2.
             03 Col-1   PIC X(100) VALUE SPACES.
          02 Linha-3.
             03 Col-1   PIC X(100) VALUE SPACES.
          02 Linha-4.
             03 Col-1   PIC X(100) VALUE SPACES.

       PROCEDURE DIVISION.
           MOVE SPACES TO Tela.

           DISPLAY 'Digite o primeiro número: ' WITH NO ADVANCING.
           ACCEPT Num1.

           DISPLAY 'Digite a operação (+, -, *, /): ' WITH NO ADVANCING.
           ACCEPT Operacao.

           DISPLAY 'Digite o segundo número: ' WITH NO ADVANCING.
           ACCEPT Num2.

           PERFORM CALCULAR-RESULTADO.

           DISPLAY 'Resultado: ' Result.

           STOP RUN.

       CALCULAR-RESULTADO.
           EVALUATE Operacao
               WHEN '+' ADD Num1 TO Num2 GIVING Result
               WHEN '-' SUBTRACT Num2 FROM Num1 GIVING Result
               WHEN '*' MULTIPLY Num1 BY Num2 GIVING Result
               WHEN '/' DIVIDE Num1 BY Num2 GIVING Result
               WHEN OTHER DISPLAY 'Operação inválida!'
           END-EVALUATE.

