from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to="media")
    logo = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title+self.name
    
