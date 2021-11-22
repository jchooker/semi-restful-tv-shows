from django.db import models
# from datetime import datetime
# from django.utils import timezone
# from time import localtime, strftime

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
