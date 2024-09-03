# scraper.py

import os
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Config

class Scraper:
    def __init__(self):
        """
        Initializes the Scraper class.
        
        Sets up the Chrome WebDriver and maximizes the browser window.
        Loads the list of codes from the specified Excel file.
        """
        service = Service(Config.CHROME_DRIVER_PATH)  # Use the Chrome driver path from config
        self.driver = webdriver.Chrome(service=service)
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        self.codes = self.load_excel()

    def load_excel(self):
        """
        Loads a list of codes from an Excel file.
        
        Returns:
            list: A list of codes extracted from the 'Code' column of the Excel file.
        """
        df = pd.read_excel(Config.EXCEL_FILE_PATH)
        return df['Code'].tolist()

    def search_and_scrape(self, code):
        """
        Searches for images related to a specific code and scrapes their URLs.
        
        Args:
            code (str): The code for which images are to be searched.
        
        Returns:
            list: A list of successfully scraped image URLs.
        """
        search_url = Config.GOOGLE_IMAGE_SEARCH_URL + code
        self.driver.get(search_url)
        time.sleep(2)

        image_urls = []
        for i in range(1, Config.IMAGES_TO_DOWNLOAD + 1):  # Use the number from config
            try:
                # Click on the div for the image
                div_xpath = Config.XPATH_BASE_DIV.format(i)
                self.driver.find_element("xpath", div_xpath).click()
                time.sleep(2)

                # Get the full resolution image URL
                image_url = self.driver.find_element("xpath", Config.XPATH_FULL_RES_IMAGE).get_attribute('src')
                image_urls.append(image_url)
                self.download_image(image_url, code, i)
            except Exception as e:
                print(f"Error retrieving image for {code} from div {i}: {e}")
                continue

        return image_urls

    def download_image(self, url, code, num):
        """
        Downloads an image from a given URL and saves it locally.
        
        Args:
            url (str): The URL of the image to be downloaded.
            code (str): The code associated with the image for folder naming.
            num (int): The image number for naming purposes.
        """
        response = requests.get(url)
        folder_path = os.path.join(Config.SCRAPED_IMAGES_PATH, f"{code}_images")
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, f"{num}.jpg"), 'wb') as file:
            file.write(response.content)

    def execute_scraping(self):
        """
        Executes the entire scraping process for all codes.
        
        Iterates through each code, scrapes images, and saves the results to a CSV file.
        """
        all_image_data = []
        for code in self.codes:
            print(f"Scraping images for code: {code}")
            image_urls = self.search_and_scrape(code)
            for url in image_urls:
                all_image_data.append({"code": code, "image_url": url})

        # Save results to CSV
        results_df = pd.DataFrame(all_image_data)
        results_df.to_csv(os.path.join(Config.SCRAPED_DATASET_PATH, 'scraped_images.csv'), index=False)

    def close(self):
        """
        Closes the WebDriver and ends the browser session.
        """
        self.driver.quit()