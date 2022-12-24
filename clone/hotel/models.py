from django.db import models

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(blank=True, max_length=400)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Hotel(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    category_id = models.ForeignKey(Category, null = True, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=400)
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    detail = models.TextField()
    star = models.FloatField()
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    location = models.CharField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# Create your models here.
