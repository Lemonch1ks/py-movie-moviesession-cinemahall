import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )

def get_movie_sessions(
        session_date: datetime.datetime = None,
) -> MovieSession | QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time=session_date)
    return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time and movie_id and cinema_hall_id:
        session.objects.update(
            show_time=show_time,
            cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
            movie=Movie.objects.get(id=movie_id),
        )

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
