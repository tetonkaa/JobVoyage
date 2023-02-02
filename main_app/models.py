from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Application(models.Model):
    date_applied = models.DateField(default=date.today)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_link = models.CharField(max_length=200, null=True)
    APPLIED = 'Applied'
    INTERVIEWING = 'Interviewing'
    PREVIOUS = 'Previous Application'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.company}, {self.position}"

STATUS_CHOICES = [
        ('A', 'Applied'),
        ('I', 'Interviewing'),
        ('P', 'Previous Application'),
    ]

class Status(models.Model):
    app_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.app_status}'