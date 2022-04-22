from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='djangoapp/static/img/')
    size = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET(1), default='1')

    def __str__(self):
        return self.name

    # redirect from adding
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
