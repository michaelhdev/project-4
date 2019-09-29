from django.test import TestCase
from .forms import FeatureForm, CommentForFeatureForm

"""Form tests for the features app """

class TestFeatureForm(TestCase):
    
    def test_cant_create_feature_with_no_info(self):
        form = FeatureForm({'title': '', 'description':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        
    def test_cant_create_feature_with_just_title(self):
        form = FeatureForm({'title': 'Test Title'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
    
    def test_cant_create_feature_with_just_description(self):
        form = FeatureForm({'description': 'Test Description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    def test_can_create_feature(self):
        form = FeatureForm({'title': 'Test', 'description':'Test Description'})
        self.assertTrue(form.is_valid())

class TestCommentForFeatureForm(TestCase):
    
    def test_cant_create_feature_with_no_comment(self):
        form = CommentForFeatureForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
        
        
    def test_can_feature_comment(self):
        form = CommentForFeatureForm({'comment': 'Test Comment'})
        self.assertTrue(form.is_valid())
        