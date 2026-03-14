# Web scraping and data storage pipeline for books.toscrape.com

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    current_url = "https://books.toscrape.com/"
    db_name = "Books.db"
    table_name = "Books"
    csv_path = "books_all_pages.csv"

    rows = []

    while current_url:
        response = requests.get(current_url)
        response.raise_for_status()
        html_page = response.text

        data = BeautifulSoup(html_page, "html.parser")
        books = data.find_all("article", class_="product_pod")

        for book in books:
            link_tag = book.find("a")
            title = link_tag["title"]
            link_book = urljoin(current_url, link_tag["href"])
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()

            rating_tag = book.find("p", class_="star-rating")
            rating = rating_tag["class"][1]

            rating_map = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5,
            }
            rating_number = rating_map[rating]

            data_dict = {
                "title": title,
                "price": price,
                "rating": rating_number,
                "availability": availability,
                "product_page_URL": link_book,
            }
            rows.append(data_dict)

        next_button = data.find("li", class_="next")
        if next_button:
            next_link = next_button.find("a")["href"]
            current_url = urljoin(current_url, next_link)
        else:
            current_url = None

    df = pd.DataFrame(rows)

    print(df.head())
    print(f"Total books scraped: {len(df)}")

    df.to_csv(csv_path, index=False)

    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()


if __name__ == "__main__":
    main()
