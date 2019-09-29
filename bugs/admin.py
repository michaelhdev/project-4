from django.contrib import admin
from .models import Bug,    CommentForBug

"""
   Register models to admin interface
"""

admin.site.register(Bug)
admin.site.register(CommentForBug)