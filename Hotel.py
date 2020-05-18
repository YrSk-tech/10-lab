class Hotel:
    hotel_type = "Budget and Value Hotels"

    def __init__(self, visitors_per_year=None, number_of_rooms=None, star_rating=None, name_of_hotel="New hotel",
                 price_uah_per_day=None, country="New country", ):
        self.visitors_per_year = visitors_per_year
        self.number_of_rooms = number_of_rooms
        self.star_rating = star_rating
        self.name_of_hotel = name_of_hotel
        self.price_uah_per_day = price_uah_per_day
        self.country = country

    @staticmethod
    def get_hotel_type():
        return Hotel.hotel_type

    def __str__(self):
        return "number of visitors per year:" + str(self.visitors_per_year) + ", number of rooms: " + str(
            self.number_of_rooms) + ", star rating:" + str(
            self.star_rating) + ", the name of the hotel:" + self.name_of_hotel + ", price in UAH per day:" + str(
            self.price_uah_per_day) + ", screen refresh rate:" + self.country

    def __del__(self):
        pass


if __name__ == "__main__":
    first_hotel = Hotel(4, 8, 256, "HP", 25000, "Ukraine")
    second_hotel = Hotel(3, 8, 256, "Apple")
    third_hotel = Hotel()

    print(first_hotel.__str__())
    print(second_hotel.__str__())
    print(third_hotel.__str__())

    print("Static field, type of hotel:" + Hotel.get_hotel_type())
