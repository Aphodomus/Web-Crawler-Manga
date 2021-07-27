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
