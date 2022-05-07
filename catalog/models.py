from django.db import models

# Create your models here.
class test(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=10)
