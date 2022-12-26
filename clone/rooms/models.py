from django.db import models

class Room(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=400)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
