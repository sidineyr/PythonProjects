% Dados para o gráfico de pizza
valores = [30, 20, 15, 10, 5];  % Valores das fatias
rotulos = {'A', 'B', 'C', 'D', 'E'};  % Rótulos das fatias

% Criar o gráfico de pizza
figure;  % Cria uma nova figura
pie(valores, rotulos);  % Cria o gráfico de pizza com os valores e rótulos especificados
title('Exemplo de Gráfico de Pizza');  % Adiciona um título ao gráfico
