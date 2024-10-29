import pandas as pd

HOTELS_DATA_PATH = "data/hotels.csv"
CARDS_DATA_PATH = "data/cards.csv"
CARDS_SEC_DATA_PATH = "data/card_security.csv"


class Hotel:
    # Load the hotels data; df is a class variable
    df = pd.read_csv(HOTELS_DATA_PATH)

    def __init__(self, hotel_id: int) -> None:
        self.id: int = hotel_id
        self.name: str = self.df.loc[self.df["id"]
                                     == self.id, "name"].squeeze()

    def available(self) -> bool:
        """Checks if the hotel is available for booking"""
        if self.df.loc[self.df["id"] == self.id, "available"].squeeze() == "yes":
            return True
        else:
            return False

    def book(self):
        """Books the hotel by changing the availability status to 'no'"""
        self.df.loc[self.df["id"] == self.id, "available"] = 'no'
        self.df.to_csv(HOTELS_DATA_PATH, index=False)

    @classmethod
    def print_all(cls):
        print(cls.df)

    @classmethod
    def count(cls):
        return cls.df.shape[0]


class SpaHotel(Hotel):
    def book_spa_package(self):
        """Books the SPA package"""
        pass


class ReservationTicket:
    def __init__(self, customer_name: str, hotel_to_book: Hotel) -> None:
        self.user_name = customer_name
        self.hotel = hotel_to_book

    def generate(self) -> str:
        self.content = f"""
            Hello {self.the_customer_name}.
            
            Thank your for your reservation!
            Your booking details are as follows:
            Name: {self.the_customer_name}
            Hotel Name: {self.hotel.name}"""
        return self.content

    @property
    def the_customer_name(self):
        return self.user_name.strip().title()


class SpaReservationTicket():
    def __init__(self, customer_name: str, spa_to_book: SpaHotel) -> None:
        self.user_name = customer_name
        self.spa = spa_to_book

    def generate(self) -> str:
        self.content = f"""
            Thank you for your SPA reservation!
            Here are your SPA booking data:
            Name: {self.the_customer_name}
            Hotel Name: {self.spa.name}"""
        return self.content

    @property
    def the_customer_name(self):
        return self.user_name.strip().title()


class CreditCard:
    # Load the credit card data; cdf is a class variable
    cdf = pd.read_csv(CARDS_DATA_PATH, dtype=str).to_dict(orient="records")

    def __init__(self, number: str) -> None:
        self.number = number

    def validate(self, expiration: str, holder: str, cvc: str) -> bool:
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in self.cdf:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    # Load the secure credit card data; scdf is a class variable
    scdf = pd.read_csv(CARDS_SEC_DATA_PATH, dtype=str)

    def authenticate(self, given_password: str) -> bool:
        password = self.scdf.loc[self.scdf["number"] ==
                                 self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(
    f"Welcome to the hotel booking system! {Hotel.count()} hotels are in stock.")
Hotel.print_all()
hotel_id: int = int(input("Enter hotel id: "))
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if not credit_card.authenticate(given_password="mypass"):
            print("Credit card authentication failed.")
            exit(1)
        hotel.book()
        user_name: str = input("Enter your name: ")
        reservation_ticket = ReservationTicket(user_name, hotel)
        print(reservation_ticket.generate())
        want_spa = input("Do you want to book a SPA packagpasse? (yes/no): ")
        if want_spa == "yes":
            hotel.book_spa_package()
            spa_reservation_ticket = SpaReservationTicket(user_name, hotel)
            print(spa_reservation_ticket.generate())
    else:
        print("Invalid credit card")
else:
    print("Hotel not available")
