# Vehicle Parts Image Scraper

This project is an image scraper script designed to retrieve full-resolution images of vehicle parts. It processes reference codes from a custom Excel dataset, performs Google Image searches for each code, and downloads the images. It then creates a new dataset that includes the URLs of the downloaded images along with their corresponding reference codes.

## Custom Excel Dataset

The custom Excel dataset used in this project contains 3 reference code:
![Example Dataset](https://github.com/user-attachments/assets/c59aaeae-a2d9-42a6-a2b2-380485b1cb9b)

## Installation

1. **Download ChromeDriver**: You can download it from [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads).

2. **Install Required Python Libraries**:
   Open your terminal and run:
   ```bash
   pip install -r requirements.txt

## To get the XPath for the elements on Google Images :

- **XPath for Base Div**:
  ![XPath Base Div](https://github.com/user-attachments/assets/e0c9ff73-fe8e-439c-924d-a81587e1f87d)
  
- **XPath for Full-Resolution Image**:
  ![XPath Full Resolution Image](https://github.com/user-attachments/assets/4eee0fee-a181-43d7-80b4-9fad0c809168)

## Ensure that the CHROME_DRIVER_PATH and other variable paths in config.py are set correctly.



