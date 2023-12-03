from django.db import models

class NewsItem(models.Model):
    source = models.CharField(max_length=100) #From what news site
    link = models.TextField()
    title = models.CharField(max_length=500)
    posted = models.CharField(max_length=100)

    def __str__(self):
        return self.title[0:50]