from django.db import models

class Author(models.Model):
    username=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=30,unique=True)
    passw=models.CharField(max_length=20)

    def __str__(self):
        return self.email