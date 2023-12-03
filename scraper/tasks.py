from celery import shared_task
import time
from .scraper import scrape_google
from celery import Celery
from newsaggregator.celery import app
from celery.utils.log import get_task_logger

URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

@app.task
def scrape_google_news():
    scrape_google(URL)
    return