import pandas as pd

DATA_PATH = "data/hotels.csv"


class Hotel:
    def __init__(self, hotel_id: int) -> None:
        self.id = hotel_id

    def available(self) -> bool:
        """Checks if the hotel is available for booking"""
        if df.loc[df["id"] == self.id, "available"].squeeze() == "yes":
            return True
        else:
            return False

    def book(self):
        """Books the hotel by changing the availability status to 'no'"""
        df.loc[df["id"] == self.id, "available"] = 'no'
        df.to_csv(DATA_PATH, index=False)


class ReservationTicket:
    def __init__(self, customer_name: str, hotel_to_book: Hotel) -> None:
        self.user_name = customer_name
        self.hotel = hotel_to_book

    def generate(self) -> str:
        self.content = f"Hello {self.user_name}, your reservation is confirmed for hotel {self.hotel.id}"
        return self.content


df = pd.read_csv(DATA_PATH)
print(df)
hotel_id: int = int(input("Enter hotel id: "))
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    user_name: str = input("Enter your name: ")
    reservation_ticket = ReservationTicket(user_name, hotel)
    reservation_ticket.generate()
    print(reservation_ticket.content)
else:
    print("Hotel not available")
