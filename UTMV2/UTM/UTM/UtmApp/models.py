from django.db import models

# Create your models here.

class HashTable(models.Model):
    hashCode=models.CharField(max_length=250,unique=True,blank=False,primary_key=True)
    link=models.TextField(blank=False,null=True)
    def __str__(self):
        return self.link