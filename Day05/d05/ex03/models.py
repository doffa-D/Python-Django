from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(null=True, max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField()    
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title
