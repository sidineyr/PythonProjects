10 PRINT "Este programa calcula a energia e a corrente em um circuito com três resistores."
20 INPUT "Digite o valor do Resistor 1 (em ohms): ", R1
30 INPUT "Digite o valor do Resistor 2 (em ohms): ", R2
40 INPUT "Digite o valor do Resistor 3 (em ohms): ", R3
50 INPUT "Digite a tensão da fonte (em volts): ", V

REM Calculando a resistência total do circuito
RT = R1 + R2 + R3

REM Calculando a corrente
I = V / RT

REM Calculando a energia
W = V * I

PRINT "A resistência total é: "; RT; " ohms"
PRINT "A corrente é: "; I; " amperes"
PRINT "A energia é: "; W; " watts"

END
