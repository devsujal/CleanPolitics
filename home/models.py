from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    date = models.DateField()

    def _str_(self):
        return self.name