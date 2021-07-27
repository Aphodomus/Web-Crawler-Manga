"""
Você foi contratado para fazer um sistema que armazena informacoes de mangás.

O cliente quer que você armazene os mangás dentro de uma pasta local no computador com o
nome "Mangas".

Voce deve criar uma pasta no computador PARA CADA manga. O nome da pasta sera o nome do proprio manga,
e dentro dele sera guardado a imagem do manga e um arquivo .txt contendo as seguintes informacoes:

0) Quantidade de membros
1) Nome do manga
2) Ano de lançamento
3) Avaliação
4) Imagem do manga
5) Descricao da manga
6) Link para os detalhes completos sobre o manga
7) Imagem QR Code contendo os detalhes resumidos do manga


Além disso, o cliente quer que você crie funcionalidades de ordenar os mangas por nome (ordem alfabetica),
por ano de lançamento e por avaliação.

Ah, e como o cliente esta pagando bem, também quer que seja possível pesquisar mangas
por nome (nomes parecidos), por ano (todos os mangas lançadas em 2017, por exemplo), e por avaliação.

Por fim, o cliente também ofereceu pagamento de hora extra para realizar uma outra atividade.
Dessa vez, ele quer um sistema de reconhecimento de voz. Ao falar um comando especifico,
o sistema deve reconhecer o comando e executa-lo.

Os comandos sao os seguintes:

- "Trailer <manga>". -> Esse comando deve abrir um video do youtube para visualizacao do trailer
da mesma

- "Detalhes <manga>" -> Ao dizer esse comando, o sistema devera falar, em voz alta,
o conteudo presente no arquivo de detalhes da serie

OBS: O conteudo original esta em ingles. Portanto, deve ser traduzido antes de ser apresentado

O site é https://myanimelist.net/topmanga.php?limit=0
"""

import os
from utils.utils import *
ROOT_PATH = os.getcwd()

def main():
    # Do a request and create a html file
    do_request()

    # Get a list content all mangas
    mangas = get_all_mangas()

    # Create all paste, image, qrcode and description about the manga
    for obs in mangas:
        name_manga = obs.name.replace(' ', '_').replace(':', '').replace('!', '').replace('-', '').replace('.', '').replace(',', '').replace('?', '')
        caminho_pasta = f'{os.path.join(ROOT_PATH, "storage", name_manga)}'
        create_paste_save_image(obs, caminho_pasta)
    

if __name__ == '__main__':
    main()
