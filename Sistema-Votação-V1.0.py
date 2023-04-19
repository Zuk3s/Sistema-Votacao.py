from datetime import date
from os import system

presidentes = list()
dados_canditado = dict()

def leiaNum(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número válido.\033[m")
        if ok:
            break
    return valor

while True:
    print('''\n=========================
    [1] Votar
    [2] Cadastrar
    [3] Lista de candidatos
    [4] Finalizar
=========================\n''')

    opção = str(input('Escolha uma opção: ')).strip()

#================================  OPÇÃO 1  ==================================================================

    if opção == '1': 
        y = 1
        system("cls")
        
        while y == 1:
            num_voto = int(input('\nInforme o número do eleitor que deseja votar (Digite [999] para parar): '))

            for n in presidentes:
                if num_voto == n['numero_eleitor']:
                    n['qnt_voto'] = n['qnt_voto'] + 1
                    print(f'\nSeu voto foi computado! Você votou no eleitor {n["nome"]}, {date.today()}')

                elif num_voto == 999:
                    y = 2
                    break

#============================  FIM OPÇÃO 1  ==================================================================
#================================  OPÇÃO 2  ==================================================================

    elif opção == '2':
        system("cls") 
        x = 1

        while x == 1:
            dados_canditado['nome'] = (str(input("\nDigite o nome de eleitor: "))).strip().capitalize()

            while True:
                dados_canditado['numero_eleitor'] = (int(input("Digite o número de eleitor: ")))

                if dados_canditado['numero_eleitor'] <= 0:
                    print("\nNúmero não aprovado! Por Favor, digite novamente.\n")
                else:
                    dados_canditado['qnt_voto'] = 0
                    presidentes.append(dados_canditado.copy())
                    dados_canditado.clear
                    break

            while True:
                opção = (str(input("Deseja continuar? [S/N] "))).strip().capitalize()[0]

                if opção == "S":
                    break
                elif opção == "N":
                    x = 2
                    break
                else:
                    print("Escolha errada! Escolha entre 'Sim' ou 'Não'.")

#============================  FIM OPÇÃO 2  ==================================================================
#================================  OPÇÃO 3  ==================================================================
        
    elif opção == '3':
        print()
        for n in presidentes:
            print(f"Candidato {n['nome']} - {n['numero_eleitor']}")

#============================  FIM OPÇÃO 3  ==================================================================
#================================  OPÇÃO 4  ==================================================================

    elif opção == '4':
        print(""" 
Candidato / Quantidade de votos
         """)
        for n in presidentes:
            print(f"""{n['nome']}  -----  {n['qnt_voto']}""")
        break

#============================  FIM OPÇÃO 4  ==================================================================

    else:
        print("Essa opção não existe! Tente novamente.")
