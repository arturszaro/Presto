from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class CategoryMenu(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class ItemMenu(models.Model):
    category = models.ForeignKey(CategoryMenu, related_name='itemsmenu', on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=256)
    ingredients = models.CharField(max_length=1000)
    price1 = models.IntegerField()
    price2 = models.IntegerField(default=0)
    

    def get_absolute_url(self):
        return '/menu/'

    def __str__(self):
        return self.title
