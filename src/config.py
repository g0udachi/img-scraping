# config.py

class Config:
    EXCEL_FILE_PATH = r"C:\Users\asus\Desktop\Automobile\my_dataset\reference_number.xlsx"
    SCRAPED_DATASET_PATH = r"C:\Users\asus\Desktop\Automobile\scraped_dataset"
    SCRAPED_IMAGES_PATH = r"C:\Users\asus\Desktop\Automobile\scraped_images"
    GOOGLE_IMAGE_SEARCH_URL = "https://www.google.com/search?hl=en&tbm=isch&q="
    
    # Chrome driver path
    CHROME_DRIVER_PATH = "C:\\Users\\asus\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe"
    
    # XPath for image divs
    XPATH_BASE_DIV = '//*[@id="rso"]/div/div/div[1]/div/div/div[{}]'
    
    # XPath for full resolution images
    XPATH_FULL_RES_IMAGE = '//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]'
    
    IMAGES_TO_DOWNLOAD = 15