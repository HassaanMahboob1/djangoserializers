from django.db import models

# Create your models here.
class Testing(models.Model):
    text = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.email