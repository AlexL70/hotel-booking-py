import pandas as pd

HOTELS_DATA_PATH = "data/hotels.csv"
CARDS_DATA_PATH = "data/cards.csv"


class Hotel:
    def __init__(self, hotel_id: int) -> None:
        self.id: int = hotel_id
        self.name: str = df.loc[df["id"] == self.id, "name"].squeeze()

    def available(self) -> bool:
        """Checks if the hotel is available for booking"""
        if df.loc[df["id"] == self.id, "available"].squeeze() == "yes":
            return True
        else:
            return False

    def book(self):
        """Books the hotel by changing the availability status to 'no'"""
        df.loc[df["id"] == self.id, "available"] = 'no'
        df.to_csv(HOTELS_DATA_PATH, index=False)


class ReservationTicket:
    def __init__(self, customer_name: str, hotel_to_book: Hotel) -> None:
        self.user_name = customer_name
        self.hotel = hotel_to_book

    def generate(self) -> str:
        self.content = f"""
            Hello {self.user_name}.
            
            Thank your for your reservation!
            Your booking details are as follows:
            Name: {self.user_name}
            Hotel Name: {self.hotel.name}"""
        return self.content


class CreditCard:
    def __init__(self, number: str) -> None:
        self.number = number

    def validate(self, expiration: str, holder: str, cvc: str) -> bool:
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in cdf:
            return True
        else:
            return False


df = pd.read_csv(HOTELS_DATA_PATH)
cdf = pd.read_csv(CARDS_DATA_PATH, dtype=str).to_dict(orient="records")
print(df)
hotel_id: int = int(input("Enter hotel id: "))
hotel = Hotel(hotel_id)
if hotel.available():
    credit_card = CreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        user_name: str = input("Enter your name: ")
        reservation_ticket = ReservationTicket(user_name, hotel)
        reservation_ticket.generate()
        print(reservation_ticket.content)
    else:
        print("Invalid credit card")
else:
    print("Hotel not available")
