from django.contrib import admin
from .models import Feature, CommentForFeature

"""Register the feature and comment models to the admin console """

admin.site.register(Feature)
admin.site.register(CommentForFeature)