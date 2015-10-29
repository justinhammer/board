from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_bio = models.TextField(null=True, blank=True)
    user_profile_pic = models.ImageField(upload_to='profile_pics')