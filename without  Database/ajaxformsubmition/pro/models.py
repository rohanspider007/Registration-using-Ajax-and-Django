from django.db import models

# Create your models here

class registration(models.Model):
    id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.First_name
