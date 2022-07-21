from typing import Optional
from django.db import models
from django.contrib.auth.models import User

class TaskApp(models.Model):
    status_choices=[
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]
    priority_choices=[
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
        ('5', 'five'),
    ]
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=2,choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    priority = models.CharField(max_length=2, choices=priority_choices)
