# main.py

from scraper import Scraper

if __name__ == "__main__":
    scraper = Scraper()
    try:
        scraper.execute_scraping()
    finally:
        scraper.close()