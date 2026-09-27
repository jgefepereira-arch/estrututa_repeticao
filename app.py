qtde_excelente = 0
qtde_ruim = 0

for i in range(50):
    entrevistado = input("Digite seu nome: ")
    idade = int(input("Insira sua idade: "))
    avaliacao = int(input("Insira sua avaliação (1=EXCELENTE; 2=BOM; 3=RUIM): "))
    if avaliacao == 1:
        qtde_excelente += 1
    elif avaliacao == 3:
        qtde_ruim += 1

print(f'Quantidade de avaliações "EXCELENTE": {qtde_excelente}')
print(f'Quantidade de avaliações "RUIM": {qtde_ruim}')