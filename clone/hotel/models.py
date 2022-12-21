from django.db import models

class Hotel(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=400)
    image = models.ImageField(blank=True, upload_to='images/')
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
    # categoryid = ForeignKey('self', blank = True, null = True, related_name = 'children', on_delete = models.CASCADE)
    # userid = ForeignKey('self', blank = True, null = True, related_name = 'children', on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



# Create your models here.
