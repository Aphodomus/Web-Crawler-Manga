import requests, os, urllib.request, qrcode
from models.manga import *

# Request a text from a site and write all content in a html file
def do_request():
    link = "https://myanimelist.net/topmanga.php?limit=0"
    resp = requests.get(link)

    with open('url_content.html', 'w', encoding='utf-8', newline='') as file:
        file.write(resp.text)

# Function just to pass line
def pass_line(file, count):
    for i in range(count):
        file.readline()

# Read the html file and return all the mangas you find
def get_all_mangas():
    list_mangas = []

    file_name = 'url_content.html'
    path_file = f'{os.path.join(os.getcwd(), file_name)}'

    with open(path_file, 'r', encoding='utf-8', newline='') as file:
        for line in file:
            if line.strip() == '<tr class=\"ranking-list\">':
                # Find the link
                pass_line(file, 4)
                line = file.readline()
                link = line[(line.find('href=') + len('href=') + 1) : (line.rfind('id') - 2)]

                # Find the image and description
                image_popularity_description = get_image_description(link)
                image = image_popularity_description[0]
                popularity = image_popularity_description[1]
                description = image_popularity_description[2]

                # Find the name
                pass_line(file, 7)
                line = file.readline()
                name = line[(line.rfind('">') + 2) : (line.rfind('</a></h3>'))]
                
                # Find the year
                pass_line(file, 2)
                line = file.readline()
                line = line.replace('- <br>', '').replace('<br>', '')
                year = line.strip()

                # Find the members
                line = file.readline()
                line = line.replace(' members', '')
                members = line.strip()
                
                # Find the rating
                pass_line(file, 5)
                line = file.readline()
                rating = line[(line.rfind('">') + 2) : (line.rfind('</span></div>'))]
                
                # Put all variables in a object
                object = Manga(name, year, rating, popularity, image, description, link, members)
                list_mangas.append(object)
                

    return list_mangas
                
# A "second scrap" in another page, to recover more information                
def get_image_description(link):
    resp = requests.get(str(link), stream=True)

    list_imagem_description_popularity = []

    for line in resp.iter_lines():
        line = str(line, encoding='utf-8')
        line.strip()
        line_treated = line[(line.rfind('">') + 1) : (line.rfind('</a></div>') + 1)]

        if line_treated == '>Add to My List<':
            # Find the image
            image = line[(line.find('data-src=') + len('data-src=') + 1) : (line.rfind('alt') - 2)]
            list_imagem_description_popularity.append(image)

        if line.find('<h2>Statistics</h2><div') != -1:
            # Find the popularity
            popularity = line[(line.rfind('n> ') + 3) : (line.rfind('</div>'))]
            list_imagem_description_popularity.append(popularity)
        
        if line.find('</div><h2><div class="floatRightHeader">') != -1:
            # Find the description
            description = line[(line.rfind('">') + 2) : (line.find('<br />'))]
            list_imagem_description_popularity.append(description)

            break


    return list_imagem_description_popularity

# Create a paste and save a imagem and your object
def create_paste_save_image(manga, path_destiny):
    try:
        os.mkdir(path_destiny)
        path_thumbnail = os.path.join(path_destiny, 'thumbnail.jpg')
        image = urllib.request.urlretrieve(manga.image, path_thumbnail)
        write_details_and_generate_qrcode(manga, path_destiny, image)
    except Exception:
        return False
    
    return True

# Create a qrcode and write the details
def write_details_and_generate_qrcode(manga, path_destiny, image):
    # Create the destiny and write information about the manga
    path = os.path.join(path_destiny, 'details.txt')
    with open(path, 'w', encoding='utf-8', newline='') as file:
        file.write(f'{manga.__str__()}')

    # Create a qrcode content information about the manga
    image_qrcode = qrcode.make(manga.information())
    image_qrcode.save(os.path.join(path_destiny, 'qr_code.jpg'))

    

