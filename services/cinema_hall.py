from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()

def create_cinema_hall(
        hall_name: str,
        hal_rows: int,
        hal_seats_in_row: int,
) -> CinemaHall:
    return  CinemaHall(
        hall_name=hall_name,
        hal_rows=hal_rows,
        seats_in_row=hal_seats_in_row,
    )
