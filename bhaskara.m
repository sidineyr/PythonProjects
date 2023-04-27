% Recebe os valores de a, b e c
a = inputdlg("Digite o valor de a: ");
a = str2double(a{1});

b = inputdlg("Digite o valor de b: ");
b = str2double(b{1});

c = inputdlg("Digite o valor de c: ");
c = str2double(c{1});

% Calcula o delta
delta = b^2 - 4*a*c;

% Verifica se delta é positivo
if delta >= 0
  % Calcula as raízes
  x1 = (-b + sqrt(delta)) / (2*a);
  x2 = (-b - sqrt(delta)) / (2*a);
  
  % Exibe o resultado
  resultado = sprintf("As raízes são: x1=%.2f e x2=%.2f", x1, x2);
else
  % Se delta for negativo, não há raízes reais
  resultado = "Não existem raízes reais";
end

% Cria a janela com o desenho do mapa cartesiano e os resultados das entradas
pkg load octave-gui

f = figure("name", "Fórmula de Bhaskara", "numbertitle", "off", "position", [200 200 600 600]);

x = linspace(-10, 10, 100);
y = a*x.^2 + b*x + c;

plot(x, y);
xlabel("Eixo x");
ylabel("Eixo y");

t = text(0, 0, resultado, "horizontalalignment", "center", "verticalalignment", "middle", "fontsize", 16);

set(t, "position", [0 8 0]);

waitfor(f);
