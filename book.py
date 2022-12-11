class Book:
    def __init__(self, dictionary_object) -> None:
        self.name = dictionary_object["name"]
        self.author = dictionary_object["author"]
        self.user_rating = dictionary_object["user_rating"]
        self.number_of_reviews = dictionary_object["number_of_reviews"]
        self.price = dictionary_object["price"]
        self.year = dictionary_object["year"]
        self.genre = dictionary_object["genre"]

