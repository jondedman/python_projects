from bs4 import BeautifulSoup
# import lxml
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles = [movie.getText() for movie in all_movies]

movie_titles.reverse()

with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
