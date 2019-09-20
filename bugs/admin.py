from django.contrib import admin
from .models import Bug,    CommentForBug

admin.site.register(Bug)
admin.site.register(CommentForBug)