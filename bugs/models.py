from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bug(models.Model):
    """
    A single bug
    """
    PENDING = 'Pending'
    INPROGRESS = 'In progress'
    COMPLETED = 'Completed'
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (INPROGRESS, 'In progress'),
        (COMPLETED, 'Completed')
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PENDING)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class CommentForBug(models.Model):
    comment = models.TextField()
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment