class CinemaHall:
    def __init__(self, number: int):
        self.number = number


    def movie_session(self, movie_name:str, customers: list, cleaning_staff: Cleaner):
        print(f"Movie {movie_name} start.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie {movie_name} end.")
        cleaning_staff.clean_hall(self.number)
