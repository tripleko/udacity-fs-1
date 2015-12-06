import media
import fresh_tomatos

#Hard coded list of Movie objects with title and other info.
movies = [media.Movie(movie_title="The Shawshank Redemption",
                      poster_image="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
                      trailer_youtube="https://www.youtube.com/watch?v=NmzuHjWmXOc",
                      release_date="14 October 1994"),
          media.Movie(movie_title="Spirited Away",
                      poster_image="http://ia.media-imdb.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3._V1_SY317_CR5,0,214,317_AL_.jpg",
                      trailer_youtube="https://www.youtube.com/watch?v=ByXuk9QqQkk",
                      release_date="20 July 2001"),
          media.Movie(movie_title="The Dark Knight",
                      poster_image="http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      trailer_youtube="https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                      release_date="18 July 2008"),
          media.Movie(movie_title="Office Space",
                      poster_image="http://ia.media-imdb.com/images/M/MV5BOTA5MzQ3MzI1NV5BMl5BanBnXkFtZTgwNTcxNTYxMTE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      trailer_youtube="https://www.youtube.com/watch?v=dMIrlP61Z9s",
                      release_date="19 February 1999")]

if __name__ == "__main__":
    fresh_tomatos.open_movies_page(movies)
