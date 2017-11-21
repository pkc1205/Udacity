import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://goo.gl/images/EKx8om",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Avatar = media.Movie("Avatar",
                        "A Story of existance of lives by pandora",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")


Khakhi = media.Movie("Khakhi",
                        "A Real Story of a Cop",
                        "https://en.wikipedia.org/wiki/Theeran_Adhigaaram_Ondru#/media/File:Theeran_Adhigaram_Ondru_Poster.jpg",
                        "https://www.youtube.com/watch?v=BcxdSTdXQpQ")


movies = [toy_story,Avatar,Khakhi]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
