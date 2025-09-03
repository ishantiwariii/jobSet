from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_number = models.CharField(max_length=15)

    WORK_STATUS_CHOICES = [
        ('experienced', "I'm experienced"),
        ('fresher', "I'm a fresher"),
    ]
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES)

    updates_opt_in = models.BooleanField(default=False)

    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    skills = models.CharField(max_length=255, default="Not specified")

    def __str__(self):
        return self.user.username
