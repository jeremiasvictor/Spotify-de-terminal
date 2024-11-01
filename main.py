#imports
from funcoes import *
import os

#main
musicas_playlist = {}
with open("playlist.txt", "rb") as arquivo :
    try:
        musicas_playlist = pickle.load(arquivo)
    except:
        with open("playlist.txt", "wb") as arquivo :
            pickle.dump(musicas_playlist, arquivo)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    opc = menu()
    match opc:
        case "0":
            with open("playlist.txt", "wb") as arquivo :
                pickle.dump(musicas_playlist, arquivo)
            break
        case "1":
            escutar_playlist(musicas_playlist)
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            nome_musica = input(Style.BRIGHT + "Digite o nome da música: " + Style.RESET_ALL)
            nome_cantor = input(Style.BRIGHT + "Digite o nome do cantor: " + Style.RESET_ALL)
            adicionar_musica(musicas_playlist, nome_musica, nome_cantor)
        case "3":
            remover_musica(musicas_playlist)
        case "4":
            exibir_playlist(musicas_playlist)
        case _:
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para voltar para o menu..." + Style.RESET_ALL)