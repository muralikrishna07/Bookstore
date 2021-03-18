from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=400,null=True)
    publisher = models.CharField(max_length=400,null=True)
    release_date = models.DateField(null=True)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.name    