class Manga:
    def __init__(self, name=None, year=None, rating=None, popularity=None, image=None, description=None, link=None, members=None):
        self.name = name
        self.year = year
        self.rating = rating
        self.popularity = popularity
        self.image = image
        self.description = description
        self.link = link
        self.members = members

    def __str__(self):
        return  f'Name: {self.name}\n' \
                f'Year: {self.year}\n' \
                f'Popularity: {self.popularity}\n' \
                f'Rating: {self.rating}\n' \
                f'Members: {self.members}\n' \
                f'Link: {self.link}\n' \
                f'Description: {self.description}\n'
    
    def information(self):
        return  f'Name: {self.name}\n' \
                f'Year: {self.year}\n' \
                f'Popularity: {self.popularity}\n' \
                f'Rating: {self.rating}\n' \
                f'Members: {self.members}\n' \
                f'Link: {self.link}\n'