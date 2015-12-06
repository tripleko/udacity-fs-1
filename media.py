"""Module for defining media classes like Video or Movie.

Only Movie is defined for this project but it could be expanded.
"""

class Movie():

    def __init__(self, movie_title, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date