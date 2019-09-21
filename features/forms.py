from django import forms
from .models import Feature, CommentForFeature


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('title', 'description')
        
class CommentForFeatureForm(forms.ModelForm):

    class Meta:
        model = CommentForFeature
        fields = ('comment',)