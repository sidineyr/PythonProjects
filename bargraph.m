% Dados fictícios
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"];
vendas = [1500, 2200, 1800, 2500, 1900];

% Criar gráfico de barras
bar(vendas)

% Configurar rótulos do eixo x
set(gca, 'XTick', 1:length(meses), 'XTickLabel', meses)

% Definir título e rótulos dos eixos
title("Vendas por Mês")
xlabel("Mês")
ylabel("Vendas")

% Mostrar grade no gráfico
grid on
