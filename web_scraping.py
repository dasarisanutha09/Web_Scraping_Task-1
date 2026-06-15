# Import required libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Website URL for scraping

url = "https://books.toscrape.com/"


# Sending request to website

response = requests.get(url)


# Checking website connection

if response.status_code == 200:
    print("Website connected successfully")

else:
    print("Connection failed")


# Convert webpage into readable format

soup = BeautifulSoup(response.text, "html.parser")


# Create empty lists to store data

book_titles = []
book_prices = []
book_ratings = []


# Finding all books

books = soup.find_all("article", class_="product_pod")


# Extracting data

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text


    rating = book.p["class"][1]


    book_titles.append(title)

    book_prices.append(price)

    book_ratings.append(rating)



# Creating DataFrame

data = {

    "Book Title": book_titles,

    "Price": book_prices,

    "Rating": book_ratings

}


df = pd.DataFrame(data)



# Saving data into Excel file

df.to_excel("books_data.xlsx", index=False, engine="openpyxl")



print("Data scraping completed successfully")

print("Excel file created")
