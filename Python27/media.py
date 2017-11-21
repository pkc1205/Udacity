import webbrowser
class Movie():
    """It is  class defined to display the trailers in the movie database """
    VALID_RATINGS=[1,2,3,4,5]
    def __init__(self,movie_title,movie_storyline,movie_poster_image_url,
                 movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        



    
