#imports
import random
import os
import pickle
import time
from colorama import Fore, Back, Style

#funcoes

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("=-"*25)
    print(Fore.GREEN + "O que você quer ouvir hoje?" + Style.RESET_ALL)
    print()
    print(Style.BRIGHT + "1) Escutar minha playlist")
    print("2) Adicionar uma música na minha playlist")
    print("3) Remover uma música da minha playlist")
    print("4) Exibir minha playlist")
    print("0) Fechar o programa" + Style.RESET_ALL)
    print("=-"*25)

    opc = input("Digite a opcão desejada: ")
    print("=-"*25)
    return opc

def barra_progresso(atual, total):#cria a barra
    comprimento_barra = 50
    proporcao_concluida = atual / total
    tempo_decorrido = time.strftime("%M:%S", time.gmtime(atual))
    tempo_total = time.strftime("%M:%S", time.gmtime(total))
    comprimento_preenchido = int(proporcao_concluida * comprimento_barra)
    
    if comprimento_preenchido < comprimento_barra:
        barra = '-' * comprimento_preenchido + 'o' + ' ' * (comprimento_barra - comprimento_preenchido - 1)
    else:
        barra = '-' * comprimento_preenchido
        
    print(f"\r{tempo_decorrido} [{barra}] {tempo_total}", end='')

def chamar_barra(duracao_total, tempo_inicio=None): #chama a barra (recursiva)
    if tempo_inicio is None:
        tempo_inicio = time.time()

    tempo_atual = time.time() - tempo_inicio
    if tempo_atual >= duracao_total:
        barra_progresso(duracao_total, duracao_total)
    else:
        barra_progresso(tempo_atual, duracao_total)
        time.sleep(0.1)
        chamar_barra(duracao_total, tempo_inicio)

def escutar_playlist(playlist): #1
    if len(playlist) == 0:
        verificar_playlist_vazia(playlist)
        return

    while True:
        limpar_tela()
        opc = input("Digite 0 para reproduzir aleatoriamente ou digite 1 para reproduzir em ordem: ")
        print("=-"*25)

        if opc == "0":
            reproduzir_aleatorio(playlist)

        elif opc == "1":
            reproduzir_em_ordem(playlist)

        else:
            print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
            continue
        
        while True:
            limpar_tela()
            print("Playlist finalizada.")
            opc = input("Digite 0 para voltar ao menu ou digite 1 para tocar a playlist novamente: ")
            print("=-"*25)
            if opc == "0":
                return
            elif opc == "1":
                break
            else:
                print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
                input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
                continue

def verificar_playlist_vazia(playlist):
    while True:
        limpar_tela()
        print(Fore.GREEN + "Sua playlist está vazia!" + Fore.RESET)
        opc = input("Digite 0 para adicionar uma música na playlist ou 1 para voltar ao menu: ")
        if opc == "0":
            nome_musica = input(Style.BRIGHT + "Digite o nome da música: " + Style.RESET_ALL)
            nome_cantor = input(Style.BRIGHT + "Digite o nome do cantor: " + Style.RESET_ALL)
            adicionar_musica(playlist, nome_musica, nome_cantor)
            break
        elif opc == "1":
            return
        else:
            print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)

def reproduzir_aleatorio(playlist):
    qtd_musicas = len(playlist)
    ja_tocadas = []

    while True:
        if len(ja_tocadas) == qtd_musicas:
            break

        indice = random.randint(0, qtd_musicas - 1)
        if indice in ja_tocadas:
            continue

        for key in playlist.keys():
            limpar_tela()
            detalhes = playlist[key].split(" - ")
            musica_title = detalhes[0].title()
            cantor_title = detalhes[1].title()
            if key == indice:
                print(Fore.GREEN + f"Tocando {musica_title}, de {cantor_title}..." + Fore.RESET)
                duracao_total = 3
                chamar_barra(duracao_total)
                ja_tocadas.append(indice)

                input(Style.BRIGHT + "\nTecle ENTER para tocar a próxima..." + Style.RESET_ALL)
                print("=-"*25)

def reproduzir_em_ordem(playlist):
    for key in sorted(playlist.keys()):
        limpar_tela()
        detalhes = playlist[key].split(" - ")
        musica_title = detalhes[0].title()
        cantor_title = detalhes[1].title()
        print(Fore.GREEN + f"Tocando {musica_title}, de {cantor_title}..." + Fore.RESET)
        duracao_total = 3
        chamar_barra(duracao_total)
        input(Style.BRIGHT + "\nTecle ENTER para tocar a próxima..." + Style.RESET_ALL)
        print("=-"*25)

def adicionar_musica(playlist, nome_musica, nome_cantor): #2
    musica_title = nome_musica.title()
    cantor_title = nome_cantor.title()
    musica_formatada = f"{musica_title} - {cantor_title}"

    variaveis_nome_musica = [nome_musica, nome_musica.upper(), nome_musica.lower(), nome_musica.title()]
    variaveis_nome_cantor = [nome_cantor, nome_cantor.upper(), nome_cantor.lower(), nome_cantor.title()]

    repetida = False
    for i in list(playlist.values()):
        detalhes = i.split(" - ")
        if detalhes[0] in variaveis_nome_musica and detalhes[1] in variaveis_nome_cantor:
            repetida = True

    if repetida:
        print("Essa música já foi adicionada a sua playlist.")
    else:
        playlist.update({len(playlist): musica_formatada})

        print("=-"*30)
        print(Fore.GREEN + f"A música {musica_title.title()}, de {cantor_title.title()}, foi adicionada a sua playlist principal!" + Fore.RESET)
                
    input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)

def remover_musica(playlist): #3
    
    if len(playlist) == 0:
        limpar_tela()
        print(Fore.GREEN + "Sua playlist está vazia!" + Style.RESET_ALL)
        input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
        print("=-"*25)
        return 

    while True:
        limpar_tela()
        opc = input("Digite 0 para remover pelo nome e 1 para remover pela posição: ")
        if opc == "0":
            musica_deletada = remover_pelo_nome(playlist)
        elif opc == "1":
            musica_deletada = remover_pela_posicao(playlist)

        else:      
            print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
            continue

        if musica_deletada is not None:
            print(Fore.GREEN + f"A música '{musica_deletada}' foi deletada da sua playlist principal!" + Fore.RESET)
        else:
            print(Fore.GREEN + "Música não encontrada na playlist." + Fore.RESET)

        atualizar_playlist(playlist)
        print("=-"*33)    
        input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
        break

def remover_pelo_nome(playlist):
    limpar_tela()
    nome = input(Style.BRIGHT + "Digite o nome da música que quer deletar: " + Style.RESET_ALL)
    variaveis_nome = [nome, nome.upper(), nome.lower(), nome.title()]
    for key in list(playlist.keys()):
        detalhes = playlist[key].split(" - ")
        if detalhes[0] in variaveis_nome:
            playlist.pop(key)
            return detalhes[0]
    return None

def remover_pela_posicao(playlist):
    while True:
        limpar_tela()
        posicao = input(Style.BRIGHT + "Digite a posição da música que quer deletar na playlist: " + Style.RESET_ALL)
        if posicao.isnumeric():
            posicao = int(posicao) - 1
            if 0 <= posicao < len(playlist):
                key_to_remove = list(playlist.keys())[posicao]
                detalhes = playlist[key_to_remove].split(" - ")
                playlist.pop(key_to_remove)
                return detalhes[0]
            else:
                print(Fore.GREEN + "Posição inválida!" + Fore.RESET)
                input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
                return None
        else:
            print(Fore.GREEN + "Entrada inválida!" + Fore.RESET)
            input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
            continue

def atualizar_playlist(playlist):
    temp_playlist = {}
    cont = 0
    for key in sorted(playlist.keys()):
        temp_playlist[cont] = playlist[key]
        cont += 1
    playlist.clear()
    playlist.update(temp_playlist)

def exibir_playlist(playlist, index=0):
    if index == 0:
        limpar_tela()
        print(Style.BRIGHT + Fore.GREEN + "Playlist principal:" + Style.RESET_ALL)
        print(Style.BRIGHT + f"{"#":<5} | {"Título":<15} | {"Cantor":<15}" + Style.RESET_ALL)
    
    if index < len(playlist):
        musica_title, cantor_title = playlist[index].split(" - ")
        print(f"{(index+1):<5} | {musica_title:<15} | {cantor_title:<15}")
        exibir_playlist(playlist, index + 1)
    else:
        if not playlist:
            print(Fore.GREEN + "Sua playlist está vazia!" + Style.RESET_ALL)
        print()
        input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
        print("=-" * 25) 

'''
def exibir_playlist(playlist): #4
        if len(playlist) == 0:
            while True:
                limpar_tela()
                print(Fore.GREEN + "Sua playlist está vazia!" + Style.RESET_ALL)
                opc = input("Digite 0 para adicionar uma música na playlist ou 1 para voltar ao menu: ")
                if opc == "0":
                    nome_musica = input(Style.BRIGHT + "Digite o nome da música: " + Style.RESET_ALL)
                    nome_cantor = input(Style.BRIGHT + "Digite o nome do cantor: " + Style.RESET_ALL)
                    adicionar_musica(playlist, nome_musica, nome_cantor)
                    break
                    
                elif opc == "1":
                    return
                else:
                    print(Fore.GREEN + "Opção inválida!" + Fore.RESET)
                    input(Style.BRIGHT + "Tecle ENTER para continuar..." + Style.RESET_ALL)
                    continue
                
        limpar_tela()
        print(Fore.GREEN + "Sua playlist principal\n" + Fore.RESET)
        print(Style.BRIGHT + f"{"#":<5} | {"Título":<15} | {"Cantor":<15}" + Style.RESET_ALL)
        for key in playlist.keys():
            detalhes = playlist[key].split(" - ")
            print(f"{(key+1):<5} | {detalhes[0]:<15} | {detalhes[1]:<15}")
        input(Style.BRIGHT + "\nTecle ENTER para voltar para o menu..." + Style.RESET_ALL)
        print("=-"*25)
'''
        
def carregar_playlist(nome_arquivo):
    try:
        with open(nome_arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}