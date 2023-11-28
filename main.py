from fastapi import FastAPI
app = FastAPI()
movies = [{"title":"Demo movie","year":"2001"}]


@app.get('/movies')
def movies_list():   #dupa definitia functiei trebuie sa punem ":". Dupa, functia trebuie sa fie indentata prin doua spatii.
  return movies   #aici returnam ceva

@app.post('/movies', status_code=201)   #in momentul in care vine un request de tip post pe /movies
def add_movie(movie: dict):  #nu ne-am batut capul sa ne gandim ce cod returnam, o face direct aplicatia prin comanda status code
  movies.append(movie)
