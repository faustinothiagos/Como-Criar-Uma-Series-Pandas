# Hello Series!!!
import pandas as pd

# Criando a series notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# Criar a Series alunos
lst_matriculas = ['M02', 'M05', 'M13', 'M14', 'M19']
lst_nomes = ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

print(notas); print('------------'); print(alunos)