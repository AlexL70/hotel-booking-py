import pandas as pd


class Hotel:
    def __init__(self, id: int) -> None:
        self.id = id

    def available(self) -> bool:
        pass

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name: str, hotel_to_book: Hotel) -> None:
        self.user_name = customer_name
        self.hotel = hotel_to_book

    def generate(self) -> str:
        self.content = f"Hello {self.user_name}, your reservation is confirmed for hotel {self.hotel.id}"
        return self.content


df = pd.read_csv("data/hotels.csv")
print(df)
id: int = int(input("Enter hotel id: "))
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    user_name: str = input("Enter your name: ")
    reservation_ticket = ReservationTicket(user_name, hotel)
    reservation_ticket.generate()
    print(reservation_ticket.content)
else:
    print("Hotel not available")
