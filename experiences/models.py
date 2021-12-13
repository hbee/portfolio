from django.db import models

class exp(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, blank=True)
    summary = models.TextField()

    def __str__(self):
        return self.title
