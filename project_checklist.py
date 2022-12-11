"""
() You must convert each dictionary from the “book_list” variable into a “Book” class object instantiation with the correct values passed into the new object instantiation.
() Each new “Book” instantiation should then be added to a “books” list variable to hold each new class instance. It is this “books” list you will use to filter and find books that match the three (3) data evaluation questions. In this project, you will utilize multiple Python files, and practice good debugging techniques, constantly testing every small chunk of code you write as you go along.  Be sure to check out the Project Walkthrough video for an idea of what this project will look like when completed!
 
Main Stories:
(2.5 points): As a data analyst, I want to make at least one commit for each evaluation question on GitHub with descriptive messages.  
(2.5 points): As a data analyst, I want to create a “Book” class within a “book.py” file with the following instance variables: 
name 
author 
user_rating 
number_of_reviews 
price 
year 
genre 

(5 points): As a data analyst, I want to instantiate a Book object for each dictionary within the “data_list” list and add the Book instantiation to a “books” list variable.  (create_book_list())
(5 points): As a data analyst, I want to determine what book had the lowest number of reviews in 2018. (Analysis 1)
(5 points): As a data analyst, I want to determine which genre (fiction/non-fiction) has appeared the most in the top 50s list and print the result to the terminal. (Analysis 2)
(5 points): As a data analyst, I want to determine what book has been in the top 50s list for the most years and print the book's title and the number of times it has appeared in the list to the terminal. (Analysis 3)
(10 points): As a data analyst, I want to utilize lambda functions and list comprehension within the code responsible for executing each evaluation question solution.
 
Bonus Stories:
(5 points): As a data analyst, I want to determine what author has shown up on the top 50's list the most and display the author in the terminal. (Bonus Analysis 1)
HINT: Only count distinct books by that author - Do not include the same book in different years within the calculation
(5 points): As a data analyst, I want to display the top book for each year based on the book's user rating & the number of reviews. (Bonus Analysis 2)
HINT: Find the top book by ordering by user rating and then ordering by number of reviews. Print the year and the book's title to the terminal. 
(5 points): As a data analyst, I want to determine which book has appeared the most in the top 50s list consecutively. (Bonus Analysis 2)
 
Setup Steps:
() Create a GitHub repository on GitHub. Remember to use a Python .gitignore and add a README! 
() Clone your repository down to your computer (referring to the Code Demo - Source Control video would be helpful here!) 
() Download the Starter Code zip file from the given repository link.
() Create your project in Visual Studio Code and move the invisible .git folder and README file to the folder where your project is located. 
() Place the “data.py”, “main.py”, and “book.py” files provided in the starter code download repository into your repository folder. 
() Make a test commit and check your repository to be sure the content has been updated! 
() Begin by reading over the  “main.py” file, which contains the primary logic of the application. 
() Create a “Book” class within the “book.py” file. The book class should have an initializer, and the initializer should define instance variables for each key present in the dictionaries within the data file. 
() Start coding the program first by going from the top of the user stories and working down. Decide how you will: 
() Loop over the list of dictionaries from the data.py file. 
() Instantiate a Book class object for each dictionary in the list from the data.py file. 
() Pass the information from each dictionary into each new Book class instantiation so the instantiation begins with the correct values for its instance variables. 
() Add each new Book instantiation to the “book_list” list variable. 
() Once you have a list of Book objects in a “books” list variable, start thinking about how you will handle each analytical evaluation question, including: 
() Using both Python lambda and list comprehension within the solution for each evaluation question user story. 
() Printing the results of the analysis question to the terminal
() Be sure to test your code as you complete each function and print a small message regarding the question being answered and your findings!

"""