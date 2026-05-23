from typing import List

from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet | Movie:
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres_id__in=genres_ids, actors_id__in=actors_ids)

    if genres_ids:
        return Movie.objects.filter(genres_id__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors_id__in=actors_ids)

    return Movie.objects.get()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title:str,
        movie_description:str,
        genres_ids: List[int] = None,
        actors_ids: List[int]=None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        for genre_id in genres_ids:
            genre = Genre.objects.get(id=genre_id)
            new_movie.genres.add(genres=genre)

    if actors_ids:
        for actor_id in actors_ids:
            actor = Actor.objects.get(id=actor_id)
            new_movie.actors.add(actors=actor)

    return new_movie
