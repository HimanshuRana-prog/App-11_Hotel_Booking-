import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv("cards.csv",dtype = str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv",dtype=str)

class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotel.csv", index= False)


    def available(self):
        """Check if the hotel is available"""
        availability =  df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
             return False




class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name:{self.hotel.name}
        """
        return content
    
hotel1 = Hotel(hotel_id = "188")
hotel2 = Hotel(hotel_id = "134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)
print(Hotel.name)



class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration":expiration,
                       "holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False
    # def pay(self):
        
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content




print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456") 
    if credit_card.validate(expiration = "12/26", holder = "JOHN SMITH",cvc = "123"):
        
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name:")
            reservation_ticket = ReservationTicket(customer_name = name,hotel_object= hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package? ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("Credit card authenatication failed.")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free.")