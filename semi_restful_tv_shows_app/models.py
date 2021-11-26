from django.db import models
from datetime import datetime
# from django.utils import timezone
# from time import localtime, strftime

class ShowManager(models.Manager):
    def basic_manager(self, postdata):
        errors= {}
        if len(Show.objects.filter(title=postdata["show_title"])) != 0:
            errors['duplicate_title'] = 'This show already exists in the database!'
        if len(postdata['show_title']) < 2 or len(postdata['show_title']) > 50:
            errors['title_length'] = "Invalid show title length"
        if len(postdata['show_network']) < 2 or len(postdata['show_network']) > 30:
            errors['network_length'] = "Invalid show network length"
        if len(postdata['show_title']) == 0:
            errors['no_title'] = "Please provide title for show"
        if len(postdata['show_network']) == 0:
            errors['no_network'] = "Please provide network name for show"
        if postdata['show_release_date'] == '':
            errors['no_release_date'] = "Please provide valid release date for show"
        return errors

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()
