#imports
from funcoes import *
import os

#main
nome_arquivo = "playlist.txt"
playlist = carregar_playlist(nome_arquivo)

while True:
    limpar_tela()
    opc = menu()

    match opc:
        case "0":
            with open("playlist.txt", "wb") as arquivo :
                pickle.dump(playlist, arquivo)
            break
        case "1":
            escutar_playlist(playlist)
        case "2":
            limpar_tela()
            nome_musica = input(Style.BRIGHT + "Digite o nome da música: " + Style.RESET_ALL)
            nome_cantor = input(Style.BRIGHT + "Digite o nome do cantor: " + Style.RESET_ALL)
            adicionar_musica(playlist, nome_musica, nome_cantor)
        case "3":
            remover_musica(playlist)
        case "4":
            exibir_playlist(playlist)
        case _:
            limpar_tela()
            print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para voltar para o menu..." + Style.RESET_ALL)