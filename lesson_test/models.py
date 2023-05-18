from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
