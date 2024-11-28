#!pip install pandas
#!pip install matplotlib 
#!pip install openpyxl 
#!pip install lxml

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataFrame = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Dados tratados.xlsx','dados')


dataFrame['energiaProduzidaCA'] = ((dataFrame['Vac[V]'] * dataFrame['Ica[A]'] * dataFrame['FP']) / 1000) * dataFrame['Período[h]']
dataFrame['energiaProduzidaCC'] = ((dataFrame['Vcc1[V MPPT1]'] * dataFrame['Icc1[A]']) / 1000) * dataFrame['Período[h]']
dataFrame['eficiencia %'] = (dataFrame['energiaProduzidaCA'] / dataFrame['energiaProduzidaCC'])*100

dataFrame['potenciaCA'] = (dataFrame['Vac[V]'] * dataFrame['Ica[A]'] * dataFrame['FP'])/100
dataFrame['potenciaCC'] = (dataFrame['Vcc1[V MPPT1]'] * dataFrame['Icc1[A]'] )/100

producaoMensalCA = dataFrame.groupby(['Ano', 'Mês'])['energiaProduzidaCA'].sum().reset_index()
eficienciaMensal = dataFrame.groupby(['Ano', 'Mês'])['eficiencia %'].sum().reset_index()

######################
producaoMensalCAPivot = producaoMensalCA.pivot(index='Mês', columns='Ano', values='energiaProduzidaCA')

producaoMensalCAPivot.plot(kind='bar', figsize=(12, 6))

#Configuracoes do grafico
plt.title('Energia Produzida Mensalmente em Cada Ano', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Energia Produzida (kWh)', fontsize=12)
plt.legend(title='Ano', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(12), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], rotation=0)

plt.tight_layout()
plt.show()
######################
eficienciaMensalPivot = eficienciaMensal.pivot(index='Mês', columns='Ano', values='eficiencia %')

eficienciaMensalPivot.plot(kind='bar', figsize=(12, 6))

#Configuracoes do grafico
plt.title('Eficiencia Mensal em Cada Ano', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Eficiencia (kWh)', fontsize=12)
plt.legend(title='Ano', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(12), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], rotation=0)

plt.tight_layout()
plt.show()
######################
producaoPorDia=dataFrame.groupby(['Dia', 'Mês', 'Ano'])['energiaProduzidaCA'].sum()
diaMaxProducaoCA = producaoPorDia.idxmax()
diaMinProducaoCA = producaoPorDia.idxmin()

diaMediaProducaoCA = producaoPorDia.mean()
diferenca = abs(producaoPorDia - diaMediaProducaoCA)
diaProximoDaMedia = diferenca.idxmin()



print(f"Dia de máxima produção (CA): {diaMaxProducaoCA[0]}/{diaMaxProducaoCA[1]}/{diaMaxProducaoCA[2]}")
print(f"Energia produzida: {producaoPorDia[diaMaxProducaoCA]:.2f} kWh")

print(f"Dia com produção mais próxima da média: {diaProximoDaMedia[0]}/{diaProximoDaMedia[1]}/{diaProximoDaMedia[2]}")
print(f"Energia produzida: {producaoPorDia[diaProximoDaMedia]:.2f} kWh")

print(f"Dia de mínima produção (CA): {diaMinProducaoCA[0]}/{diaMinProducaoCA[1]}/{diaMinProducaoCA[2]}")
print(f"Energia produzida: {producaoPorDia[diaMinProducaoCA]:.2f} kWh")

##########################################
#filtrar os dados para o dia de maxima producao
dadosDiaMaxProducaoCA = dataFrame[
    (dataFrame['Dia'] == diaMaxProducaoCA[0]) & 
    (dataFrame['Mês'] == diaMaxProducaoCA[1]) & 
    (dataFrame['Ano'] == diaMaxProducaoCA[2])
]
dadosDiaMaxProducaoCA['Tempo_horas'] = dadosDiaMaxProducaoCA['Hora'] + dadosDiaMaxProducaoCA['Minuto'] / 60

plt.figure(figsize=(12, 6))
plt.subplot(2,1,1)
plt.plot(dadosDiaMaxProducaoCA['Tempo_horas'], dadosDiaMaxProducaoCA['potenciaCA'], label='Potência CA (kW)',  color='blue')
plt.plot(dadosDiaMaxProducaoCA['Tempo_horas'], dadosDiaMaxProducaoCA['eficiencia %'], label='Eficiência (%)', marker='x', color='green')

#configuracoes do grafico
plt.title(f"Produção e Eficiência - {diaMaxProducaoCA[0]}/{diaMaxProducaoCA[1]}/{diaMaxProducaoCA[2]}", fontsize=14)
plt.xlabel('Tempo (horas decimais)', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.subplot(2,1,2)
plt.scatter(dadosDiaMaxProducaoCA['potenciaCA'], dadosDiaMaxProducaoCA['eficiencia %'], alpha=0.5, c='yellow')
plt.xlabel('Potência CA (kW)')
plt.ylabel('Eficiência (%)')

plt.tight_layout()
plt.show()
###########################################
#filtrar os dados para o dia mais prximo da media
dadosDiaMediaProducaoCA = dataFrame[
    (dataFrame['Dia'] == diaProximoDaMedia[0]) & 
    (dataFrame['Mês'] == diaProximoDaMedia[1]) & 
    (dataFrame['Ano'] == diaProximoDaMedia[2])
]
dadosDiaMediaProducaoCA['Tempo_horas'] = dadosDiaMediaProducaoCA['Hora'] + dadosDiaMediaProducaoCA['Minuto'] / 60

plt.figure(figsize=(12, 6))
plt.subplot(2,1,1)
plt.plot(dadosDiaMediaProducaoCA['Tempo_horas'], dadosDiaMediaProducaoCA['potenciaCA'], label='Potência CA (kW)',  color='blue')
plt.plot(dadosDiaMediaProducaoCA['Tempo_horas'], dadosDiaMediaProducaoCA['eficiencia %'], label='Eficiência (%)', marker='x', color='green')

# Configuracoes do grafico
plt.title(f"Produção e Eficiência - {diaProximoDaMedia[0]}/{diaProximoDaMedia[1]}/{diaProximoDaMedia[2]}", fontsize=14)
plt.xlabel('Tempo (horas decimais)', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.subplot(2,1,2)
plt.scatter(dadosDiaMediaProducaoCA['potenciaCA'], dadosDiaMediaProducaoCA['eficiencia %'], alpha=0.5, c='yellow')
plt.xlabel('Potência CA (kW)')
plt.ylabel('Eficiência (%)')

plt.tight_layout()
plt.show()
###########################################
#filtrar os dados para o dia de min producao
dadosDiaMinProducaoCA = dataFrame[
    (dataFrame['Dia'] == diaMinProducaoCA[0]) & 
    (dataFrame['Mês'] == diaMinProducaoCA[1]) & 
    (dataFrame['Ano'] == diaMinProducaoCA[2])
]
dadosDiaMinProducaoCA['Tempo_horas'] = dadosDiaMinProducaoCA['Hora'] + dadosDiaMinProducaoCA['Minuto'] / 60

plt.figure(figsize=(12, 6))
plt.subplot(2,1,1)
plt.plot(dadosDiaMinProducaoCA['Tempo_horas'], dadosDiaMinProducaoCA['potenciaCA'], label='Potência CA (kW)',  color='blue')
plt.plot(dadosDiaMinProducaoCA['Tempo_horas'], dadosDiaMinProducaoCA['eficiencia %'], label='Eficiência (%)', marker='x', color='green')

#Configuracoes do grafico
plt.title(f"Produção e Eficiência - {diaMinProducaoCA[0]}/{diaMinProducaoCA[1]}/{diaMinProducaoCA[2]}", fontsize=14)
plt.xlabel('Tempo (horas decimais)', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.subplot(2,1,2)
plt.scatter(dadosDiaMinProducaoCA['potenciaCA'], dadosDiaMinProducaoCA['eficiencia %'], alpha=0.5, c='yellow')
plt.xlabel('Potência CA (kW)')
plt.ylabel('Eficiência (%)')


plt.tight_layout()
plt.show()
