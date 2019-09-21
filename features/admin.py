from django.contrib import admin
from .models import Feature, CommentForFeature

admin.site.register(Feature)
admin.site.register(CommentForFeature)