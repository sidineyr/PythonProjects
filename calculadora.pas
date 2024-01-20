program Calculadora;

var
  num1, num2, resultado: real;
  operacao: char;

begin
  write('Digite o primeiro número: ');
  readln(num1);

  write('Digite a operação (+, -, *, /): ');
  readln(operacao);

  write('Digite o segundo número: ');
  readln(num2);

  case operacao of
    '+': resultado := num1 + num2;
    '-': resultado := num1 - num2;
    '*': resultado := num1 * num2;
    '/': begin
           if num2 <> 0 then
             resultado := num1 / num2
           else
           begin
             writeln('Erro: Divisão por zero!');
             halt;  // Encerra o programa com código de erro
           end;
         end;
  else
    writeln('Operação inválida!');
    halt;  // Encerra o programa com código de erro
  end;

  writeln('Resultado: ', resultado);
end.

