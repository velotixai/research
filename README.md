# Project Gutenberg Book Downloader

A simple Python script to download random books from Project Gutenberg's collection.

## Features

- Downloads books from Project Gutenberg
- Configurable number of books to download
- Creates a `data/books` directory to store downloaded books
- Handles download failures gracefully
- Includes polite delays between downloads to respect server resources

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
To download the default number of books (5):
```bash
python setup.py
```

### Custom Number of Books
To download a specific number of books, use the `-n` or `--num-books` option:
```bash
python setup.py -n 10  # Downloads 10 books
```

### Output
- Books are downloaded to the `data/books` directory
- Each book is saved as a text file named `book_[ID].txt`
- The script shows progress during downloads and reports success/failure for each book

## Notes

- The script focuses on books with IDs between 1 and 1000 (generally more popular books)
- If a book download fails, the script will automatically try another book
- A 1-second delay is added between downloads to be polite to the Project Gutenberg servers
- The script will stop when it has successfully downloaded the requested number of books or exhausted all attempts

## Requirements

- Python 3.6+
- requests==2.31.0
