from django.db import models

class exp(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=300, blank=True)

