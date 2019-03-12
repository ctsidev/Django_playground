# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True)
    # date_posted = models.DateTimeField(auto_now_add=True)  # cannot update
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

REQUEST_TYPE_CHOICES = (
        ('Specialized Counts', 'Specialized Counts'),
        ('Limited Data Set', 'Limited Data Set'),
        ('De-Identified Dataset', 'De-Identified Dataset'),
        ('Identified Dataset', 'Identified Dataset'),
    )

class Project(models.Model):
    title = models.CharField(max_length=200)
    irb = models.CharField(max_length=20)
    
    description = models.CharField(max_length=200) 
    investigator = models.CharField(max_length=100)
    investigator_phone = models.CharField(max_length=100)
    investigator_email = models.CharField(max_length=100)
    requestor = models.CharField(max_length=100)
    requestor_phone = models.CharField(max_length=100)
    requestor_email = models.EmailField(max_length=100)
    chart_review = models.BooleanField()
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES, default='Identified Dataset')
    date_deadline = models.DateField(default=date.today)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # def is_upperclass(self):
    #     return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})