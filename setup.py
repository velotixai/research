import os
import argparse
import random
import requests
from pathlib import Path
import time

def setup_directories():
    """Create necessary directories if they don't exist."""
    Path("data/books").mkdir(parents=True, exist_ok=True)

def get_book_url(book_id):
    """Generate the URL for a Project Gutenberg book."""
    return f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"

def download_book(book_id, output_dir):
    """Download a single book and save it to the output directory."""
    try:
        url = get_book_url(book_id)
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            # Save the book
            output_file = os.path.join(output_dir, f"book_{book_id}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            return True, f"book_{book_id}"
        else:
            return False, f"HTTP status code: {response.status_code}"
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description='Download books from Project Gutenberg')
    parser.add_argument('-n', '--num-books', type=int, default=5,
                      help='Number of books to download (default: 5)')
    args = parser.parse_args()
    
    # Setup directories
    setup_directories()
    output_dir = "data/books"
    
    print(f"Will attempt to download {args.num_books} books...")
    
    # Get random book IDs (focusing on more popular books with lower IDs)
    book_ids = random.sample(range(1, 1000), args.num_books * 2)
    
    # Download books
    successful_downloads = 0
    attempted_ids = 0
    
    while successful_downloads < args.num_books and attempted_ids < len(book_ids):
        book_id = book_ids[attempted_ids]
        print(f"\nAttempting to download book ID {book_id}...")
        
        success, result = download_book(book_id, output_dir)
        if success:
            print(f"Successfully downloaded: {result}")
            successful_downloads += 1
        else:
            print(f"Failed to download book {book_id}: {result}")
        
        # Add a small delay between downloads to be polite to the server
        time.sleep(1)
        attempted_ids += 1
    
    print(f"\nDownload complete! Successfully downloaded {successful_downloads} books to {output_dir}")

if __name__ == "__main__":
    main() 