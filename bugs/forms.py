from django import forms
from .models import Bug, CommentForBug

"""
    Form declarations for bugs app
"""
class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('title', 'description')
        
class CommentForBugForm(forms.ModelForm):

    class Meta:
        model = CommentForBug
        fields = ('comment',)