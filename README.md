# Spotify de Terminal (Simulador de Player de Música)

Este projeto é um simulador de player de música desenvolvido como parte de uma atividade acadêmica na universidade para obtenção de nota. O player de música funciona no terminal e permite aos usuários gerenciar uma lista de reprodução de músicas de forma simples e intuitiva. As funcionalidades incluem simular a reprodução de música, adicionar e remover músicas da playlist, e exibir a lista de reprodução. A playlist é carregada e salva em um arquivo de texto (playlist.txt). As bibliotecas utilizadas no projeto são random, os, pickle, time e colorama.

## Instalação

Antes de começar, certifique-se de ter o Python instalado na sua máquina. Você pode baixar o Python no site oficial.

Passos para Instalação:
1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/jeremiasvictor/Spotify-de-terminal.git
```

2. Navegue até o diretório do projeto:

```bash
cd Spotify-de-terminal
```

3. (Opcional) Crie um ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

4. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Uso
Após a instalação, você pode executar o código para iniciar o player de música no terminal. Ao iniciar, será exibido um menu com as seguintes opções:

- Teclar 1: Simula a reprodução de uma música da playlist.
- Teclar 2: Permite ao usuário adicionar uma nova música à playlist.
- Teclar 3: Permite ao usuário remover uma música existente da playlist.
- Teclar 4: Mostra todas as músicas atualmente na playlist.
- Teclar 0: Encerra o programa. 

### Exemplo de Uso

Execute o script principal do projeto:
python main.py

O menu será exibido no terminal, digite o número correspondente à ação que deseja realizar e siga as instruções subsequentes.

## Contribuição
Contribuições são bem-vindas! Se você gostaria de contribuir com o projeto, por favor, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas alterações (git commit -m 'Adiciona nova feature').
4. Faça push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.
   
## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autores
Jeremias Victor Marinho Santos

## Tecnologias
Este projeto foi desenvolvido utilizando as seguintes tecnologias:

1. Python
2. Bibliotecas: random, os, pickle, time, colorama
