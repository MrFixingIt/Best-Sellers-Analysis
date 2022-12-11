from data import data_list
from book import Book

def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)

# ------------------------------------- create_book_list(data_list) ---------------------------------------------------
def create_book_list(data_list):
    book_list = []
    # TODO: Write a function that will loop through data_list, and create a Book object for each list item
    for book in data_list:
        book_object = Book(book)
        book_list.append(book_object)
    # TODO: Then, add each Book item to book_list
    # TODO: Finally, return book_list for use in analysis questions!
    return book_list

# ------------------------------------- example_analysis(book_list) ---------------------------------------------------
def example_analysis(book_list):
    print("Example Analysis:")
    print("Which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} for ${highest_cost_book.price}.")

# ------------------------------------- analysis_one(book_list) ---------------------------------------------------
def analysis_one(book_list):
    print("Analysis One:")
    print("Which book had the lowest number of reviews in 2018?")
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    lowest_review_book = min(books_2018, key=lambda book: book.number_of_reviews)
    print(f"The book with the lowest number of reviews in 2018 was {lowest_review_book.name} with {lowest_review_book.number_of_reviews} reviews.")

# ------------------------------------- analysis_two(book_list) ---------------------------------------------------
def analysis_two(book_list):
    print("Analysis Two:")
    print("Which genre (fiction or non-fiction) has appeared the most in the top 50's list?")
    book_set = set(book_list)
    fiction_set_appearances = set(filter(lambda book: book.genre == "Fiction", book_set))
    nonfiction_set_appearances = set(filter(lambda book: book.genre == "Non Fiction", book_set))
    number_of_fiction_appearances = len(fiction_set_appearances)
    number_of_nonfiction_appearances = len(nonfiction_set_appearances)

    if number_of_fiction_appearances > number_of_nonfiction_appearances:
        print(f"Fiction books appeared the most in the top 50's list.")
    elif number_of_nonfiction_appearances > number_of_fiction_appearances:
        print(f"Non Fiction books appeared the most in the top 50's list.")
    else:
        print("There are an equal number of Fiction genre books as Non Fiction genre books.")

# ------------------------------------- analysis_three(book_list) ---------------------------------------------------
def analysis_three(book_list):
    print("Analysis Three:")
    print("Which book has appeared the most in the top 50's list, and how many times has it appeared?")
    book_name_list = [book.name for book in book_list]
    top_book = {"name": "book name", "count": 0}
    unique_book_names = set(book_name_list)
    for book_name in unique_book_names:
        results = len(
            list(filter(lambda name: name == book_name, book_name_list)))
        if results > top_book["count"]:
            top_book["name"] = book_name
            top_book["count"] = results
    print(f'Book Title: {top_book["name"]} has the most appearances. Frequency: {str(top_book["count"])}.')

# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
