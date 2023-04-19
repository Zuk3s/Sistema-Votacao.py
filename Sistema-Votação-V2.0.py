from datetime import date
from os import system

presidentes = list()
dados_canditado = dict()
data_atual = date.today()
data_brasil = data_atual.strftime('%d/%m/%Y %H:%M')


def leiaNum(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print("\033[0;31mERRO! Digite um número válido.\033[m")


def leiaString(msg):
    while True:
        pergunta = str(input(msg)).strip().capitalize()
        if pergunta.isalpha():
            return pergunta
        else:
            print("\033[0;31mERRO! Digite uma opção válida.\033[m")


def listaCandidato(votos = True):
        for candidatos in presidentes:
            if(votos):
                print(f"{candidatos['nome']} - {candidatos['qnt_voto']}")
            else:
                print(f"Candidato {candidatos['nome']} - {candidatos['numero_eleitor']}")


while True:
    print('''\n=========================
    [1] Votar
    [2] Cadastrar
    [3] Lista de candidatos
    [4] Finalizar
=========================\n''')

    opção = leiaNum('Escolha uma opção: ')

    if opção == 1:
        exit = False
        system("cls")

        listaCandidato(votos=False)
        print()

        while not exit:
            num_voto = leiaNum('\nInforme o número do eleitor que deseja votar (Digite [999] para parar): ')

            for candidato in presidentes:
                if num_voto == candidato['numero_eleitor']:
                    candidato['qnt_voto'] = candidato['qnt_voto'] + 1
                    print(f'\nSeu voto foi computado! Você votou no eleitor {candidato["nome"]}, {data_brasil}')
                elif num_voto == 999:
                    exit = True
                    break

    elif opção == 2:
        system("cls")
        exit = False

        while not exit:
            dados_canditado['nome'] = leiaString("\nDigite o nome de eleitor: ")

            while True:
                dados_canditado['numero_eleitor'] = leiaNum("Digite o número de eleitor: ")

                if dados_canditado['numero_eleitor'] <= 0:
                    print("\nNúmero não aprovado! Por Favor, digite novamente.")
                else:
                    dados_canditado['qnt_voto'] = 0
                    presidentes.append(dados_canditado.copy())
                    dados_canditado.clear
                    break

            while True:
                opção = leiaString("Deseja continuar? [S/N] ")[0]

                if opção == "S":
                    break
                elif opção == "N":
                    exit = True
                    break
                else:
                    print("Escolha errada! Escolha entre 'Sim' ou 'Não'.")

    elif opção == 3:
        system("cls")
        print('='*25, '\n')
        listaCandidato(votos=False)

    elif opção == 4:
        system("cls")
        print(""" 
Candidato / Quantidade de votos
         """)
        listaCandidato()
        break

    else:
        print("Essa opção não existe! Tente novamente.")
