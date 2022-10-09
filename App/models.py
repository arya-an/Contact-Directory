from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    PhnNo = models.CharField(max_length=50)
    def __str__(self):
        return self.Name