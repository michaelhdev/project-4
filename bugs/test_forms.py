from django.test import TestCase
from .forms import BugForm, CommentForBugForm

class TestBugForm(TestCase):
    
    def test_cant_create_bug_with_no_info(self):
        form = BugForm({'title': '', 'description':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        
    def test_cant_create_bug_with_just_title(self):
        form = BugForm({'title': 'Test Title'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
    
    def test_cant_create_bug_with_just_description(self):
        form = BugForm({'description': 'Test Description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    def test_can_create_bug(self):
        form = BugForm({'title': 'Test', 'description':'Test Description'})
        self.assertTrue(form.is_valid())

class TestCommentForBugForm(TestCase):
    
    def test_cant_create_bug_with_no_comment(self):
        form = CommentForBugForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
        
        
    def test_can_bug_comment(self):
        form = CommentForBugForm({'comment': 'Test Comment'})
        self.assertTrue(form.is_valid())
        