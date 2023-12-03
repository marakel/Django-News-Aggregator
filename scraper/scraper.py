from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import datetime
from dateutil.relativedelta import relativedelta
from .models import NewsItem


def scrape_google(url):
    options = webdriver.ChromeOptions()
    options.add_argument(" -incognito")

    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "f9uzM"))
        )
        time.sleep(0.5)

    except:
        driver.quit()

    
    try:
        article_elements = driver.find_elements(By.CLASS_NAME, "IBr9hb")
        for article in article_elements:
            link = article.find_element(By.CSS_SELECTOR, "a")

            #Article Links
            news_item_link = link.get_attribute('href')

            #Article title
            title = article.find_element(By.CLASS_NAME, "gPFEn")
            news_item_title = title.get_attribute('innerHTML')

            #Article time posted
            posted = article.find_element(By.CLASS_NAME, "hvbAAd")
            news_item_posted = posted.get_attribute('innerHTML')

            #Article source
            source = article.find_element(By.CLASS_NAME, "vr1PYe")
            news_item_source = source.get_attribute('innerHTML')

            NewsItem.objects.get_or_create(
                title=news_item_title,
                link=news_item_link,
                posted=news_item_posted,
                source=news_item_source,
            )
    except:
        pass
