from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from bugs.models import CommentForBug


class Feature(models.Model):
    """
    A single feature
    """
    PENDING = 'pending'
    INPROGRESS = 'progressed'
    COMPLETED = 'completed'
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (INPROGRESS, 'In progress'),
        (COMPLETED, 'Completed')
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PENDING)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)
    comments = models.ManyToManyField(CommentForBug, related_name='votes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class CommentForFeature(models.Model):
    comment = models.TextField()
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment