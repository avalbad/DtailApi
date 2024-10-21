from django.db import models

# Create your models here.
class MyObject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    number = models.IntegerField()