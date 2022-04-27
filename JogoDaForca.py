from time import sleep
import random

lista_de_palavras = ['banana', 'melancia', 'abacaxi', 'computador']


def main():
    print("#############################")
    print("BEM VINDO AO JOGO DA FORCA.PY")
    print("#############################")
    print('\n')
    sleep(1)
    menu()


def menu():
    print("#############################")
    print("########### MENU ############")
    print("#############################")

    print("Selecione alguma opção digitando um número:")
    print("1-Jogar")
    print("2-Listar palavras")
    print("3-Cadastrar palavras")
    print("4-Sair do jogo")

    opcao = input("Opção: ")

    if opcao == "1":
        iniciar_jogo()
    elif opcao == "2":
        listar_palavras()
    elif opcao == "3":
        cadastrar_palavras()
    elif opcao == "4":
        sair_do_jogo()
    else:
        print("Insira uma opção válida ;P")
        sleep(1)
        menu()


def iniciar_jogo():
    print("//////////////////////////////")
    print("######## VAMOS JOGAR! ########")
    print("//////////////////////////////")
    print("--------------------------------------------")
    print("Digite uma letra e tente adivinhar a palavra")
    print("--------------------------------------------")
    sleep(1)
    adivinhacao()


def listar_palavras():
    print("As palavras cadastradas são: ")
    indice = 1
    for i in lista_de_palavras:
        print(indice, "-", i)
        indice += 1
    
    sleep(3)
    menu()
def cadastrar_palavras():
    print("#### CADASTRAR PALAVRAS ####")
    print("----------------------------")
    cadastro = input("Digite a palavra desejada: ")
    simbolos = "!@#$%¨&*((){}^`:?;§¨´`,.ªº[]?/|\_-'+=~1234567890"
    gaps = " "
    for index in cadastro:
        for sin in simbolos:
            if index == sin or index == gaps:
                print("Palavra inválida")
                cadastrar_palavras()
                sleep(0.5)
    if len(cadastro) <= 3:
        print("Palavra inválida, a palavra deve ter mais de três letras")
        cadastrar_palavras()
        sleep(0.5)
    if cadastro in lista_de_palavras:
        print("Esta palavra ja está cadastrada")
        cadastrar_palavras()
  
    lista_de_palavras.append(cadastro)      
    print("Palavra cadastrada com sucesso")
    menu()
    
def sair_do_jogo():
    print("Até logo!")
    pass

# Parte da jogabilidade
def fim_do_jogo():
    print("-----------------------")
    print("Selecione uma opção: ")
    print("1- Jogar novamente")
    print("2- Ir para o menu")
    print("3- Sair do jogo")
    
    select = input("Opção: ")
    
    if select == "1":
        adivinhacao()
    if select == "2":
        main()
    if select == "3":
        sair_do_jogo()
    else:
        print("Opção inválida, favor inserir um dos números abaixo")
        fim_do_jogo()


def venceu():
    print("Parabéns! Voce venceu!")
    print("É um baita adivinhador!")
    sleep(1)
    fim_do_jogo()
    
def perdeu():
    print("Você mamou :(")
    print("Quem sabe na próxima")
    sleep(1)
    fim_do_jogo()
        
def adivinhacao():
    palavra_secreta = random.choice(lista_de_palavras)
    espacos_preparo = ["_"] * len(palavra_secreta)
    espacos = espacos_preparo
    
    forca1 =("------|\n"
           "|     O \n"
           "|       \n"
           "|      \n"
           "|       \n"
           "|__________")

    forca2 =("-----|\n"
           "|    O \n"
           "|    |  \n"
           "|      \n"
           "|       \n"
           "|__________")
    
    forca3 =("-----|\n"
           "|    O \n"
           "|  --|  \n"
           "|      \n"
           "|       \n"
           "|__________")
    
    forca4 =("-----|\n"
           "|    O \n"
           "|  --|--\n"
           "|      \n"
           "|       \n"
           "|__________")
    
    forca5 =("-----|\n"
           "|    O \n"
           "|  --|--\n"
           "|    | \n"
           "|       \n"
           "|__________")
    
    forca6 =("-----|\n"
           "|    O \n"
           "|  --|--\n"
           "|    | \n"
           "|   /   \n"
           "|__________")
    
    forca7 =("-----|\n"
           "|    O \n"
           "|  --|--\n"
           "|    | \n"
           "|   / \ \n"
           "|__________")
    
    acertos = 0
    erros = 0
    enforcou = False
    acertou = False

    print("SINBORA!")
    sleep(0.5)
    print("Sua palavra está assim: ")
    print(espacos)
    sleep(1)

    while not enforcou and not acertou: 
    
        chute = input("Digite uma letra: ")
    
        if len(chute) > 1:
            while len(chute) > 1:
                print("Mano eu disse UMA LETRA!")
                chute = input("Digite uma letra: ")
    
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():
                    espacos[posicao] = letra
                posicao += 1
                acertos += 1
            print(espacos)
        else:
            erros += 1
            print("Errou :(")
            if erros == 1:
                print(forca1)
                print(espacos)
            elif erros == 2:
                print(forca2)
                print(espacos)
            elif erros == 3:
                print(forca3)
                print(espacos)
            elif erros == 4:
                print(forca4)
                print(espacos)
            elif erros == 5:
                print(forca5)
                print(espacos)
            elif erros == 6:
                print(forca6)
                print(espacos)
            elif erros == 7:
                print(forca7)
                print(espacos)
        
        enforcou = erros == 7
        acertou = "_" not in espacos
        
        if acertou:
            sleep(2)
            venceu()
        elif enforcou:
            sleep(1)
            perdeu()
            
main()
