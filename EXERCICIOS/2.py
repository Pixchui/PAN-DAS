import pandas as pd

conteudo = """jogo,genero,nota,preco,ano,plataforma
The Witcher 3,RPG,93,79.90,2015,PC
Celeste,Plataforma,91,36.99,2018,Multi
Hades,Roguelike,93,46.99,2020,Multi
Stardew Valley,Simulação,89,24.99,2016,Multi
Hollow Knight,Metroidvania,90,27.99,2017,Multi
Elden Ring,RPG,96,199.90,2022,Multi
Undertale,RPG,92,21.99,2015,PC
Cuphead,Plataforma,86,37.99,2017,Multi
Dead Cells,Roguelike,89,49.90,2018,Multi
Terraria,Sandbox,83,17.99,2011,PC
Minecraft,Sandbox,93,119.90,2011,Multi
Disco Elysium,RPG,97,69.90,2019,PC
Portal 2,Puzzle,95,19.99,2011,PC
Ori and the Blind Forest,Metroidvania,88,39.99,2015,Multi
Shovel Knight,Plataforma,90,54.90,2014,Multi"""
 
with open('EXERCICIOS/jogos.csv', 'w', encoding='utf-8') as f:
    f.write(conteudo)

df = pd.read_csv('EXERCICIOS/jogos.csv')

df['genero'].value_counts()            # Minha previsão: Quantidades de um valor na coluna 'genero'.
df['nota'].max()                       # Minha previsão: Valor máximo da coluna 'nota'.
df['preco'].min()                      # Minha previsão: Valor mínimo da coluna 'preco'.
df.loc[5, 'jogo']                      # Minha previsão: Valor da linha 5 e coluna 'jogo'.
df.iloc[0:3, 1:3]                      # Minha previsão: Valores das linhas 0 a 2 e colunas 1 a 2 (excluindo a coluna 3).
df[['jogo', 'ano']].tail(3)            # Minha previsão: Valores das ultimas 3 linhas das colunas 'jogo' e 'ano'.
df.describe().loc['mean']              # Minha previsão: Média de todas as colunas numéricas.