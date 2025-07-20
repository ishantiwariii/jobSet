from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='jobs/',default='default.jpg')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)


class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
