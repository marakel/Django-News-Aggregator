from django.urls import path, include
from .views import NewsItemListView

urlpatterns = [
    path("", NewsItemListView.as_view(), name="news-item-list"),
    #path('history/', ScrapeRecordListView.as_view(), name='scrape-history')
]