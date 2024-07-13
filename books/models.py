from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.title
