# Analise-Producao-e-Eficiencia-Energetica-em-py
Este script em Python realiza a análise de dados energéticos de um sistema fotovoltaico, utilizando a biblioteca pandas para manipulação dos dados, matplotlib para visualização e numpy para cálculos.

<!DOCTYPE html>
<html>
<head>
    <title>Análise de Produção de Energia</title>
</head>
<body>
    <h1>Análise de Produção de Energia</h1>
    <p>Este projeto realiza a análise de produção e eficiência de um sistema de geração de energia, utilizando dados armazenados em uma planilha Excel.</p>
    <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Cálculo de Energia Produzida:</strong> 
            <ul>
                <li>Energia CA e CC.</li>
                <li>Eficiência percentual.</li>
            </ul>
        </li>
        <li><strong>Análise Mensal:</strong>
            <ul>
                <li>Produção mensal por ano.</li>
                <li>Eficiência média mensal.</li>
                <li>Gráficos comparativos.</li>
            </ul>
        </li>
        <li><strong>Identificação de Dias-Chave:</strong>
            <ul>
                <li>Dia de maior, menor e média de produção.</li>
            </ul>
        </li>
        <li><strong>Visualização por Dia:</strong>
            <ul>
                <li>Gráficos de potência e eficiência ao longo do dia.</li>
                <li>Dispersão entre potência e eficiência.</li>
            </ul>
        </li>
    </ul>
    <h2>Como Utilizar</h2>
    <ol>
        <li>Certifique-se de que as bibliotecas necessárias estão instaladas:
            <pre>pip install pandas matplotlib openpyxl lxml</pre>
        </li>
        <li>Substitua o caminho para o arquivo Excel no código.</li>
        <li>Execute o script em um ambiente Python com suporte a gráficos.</li>
    </ol>
    <h2>Saídas Geradas</h2>
    <ul>
        <li>Gráficos de barras comparando produção e eficiência mensalmente.</li>
        <li>Gráficos detalhados de dias com maior, menor e média de produção.</li>
    </ul>
    <h2>Estrutura do Código</h2>
    <ol>
        <li>Leitura dos dados.</li>
        <li>Processamento e cálculos.</li>
        <li>Geração de gráficos mensais e diários.</li>
        <li>Identificação e visualização de dias relevantes.</li>
    </ol>
</body>
</html>

