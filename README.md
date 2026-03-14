# Books to Scrape Web Crawler

This project implements a Python web scraper that crawls the demo website **books.toscrape.com** and extracts information about all books listed across the catalogue pages.

The script automatically follows pagination and collects book metadata into a structured dataset.

## Features

- Crawls all catalogue pages automatically
- Extracts book metadata:
  - title
  - price
  - rating
  - availability
  - product page URL
- Stores results in:
  - CSV dataset
  - SQLite database

## Technologies Used

- Python
- requests
- BeautifulSoup
- pandas
- SQLite

## How to Run

Install dependencies:
`pip install -r requirements.txt`

Run the scraper:
`python books_scraper.py`

The script will generate:
`books_all_pages.csv`
`Books.db`
containing the full dataset of scraped books.

## Purpose

This project demonstrates a complete **web scraping and data pipeline workflow**, including data extraction, transformation, and loading into persistent storage formats.
