from django.test import TestCase
from .models import Feature, CommentForFeature
from django.contrib.auth.models import User

"""Model tests for the features app """

class TestFeatureModel(TestCase):

    def test_feature_creation(self):
        user = User(username="testUser")
        user.save()
        feature = Feature(title="Test Title",description="Test Description",status="progressed",author=user)
        feature.save()
        self.assertEqual(feature.title, "Test Title")
        
class TestCommentModel(TestCase):

    def test_comment_creation(self):
        user = User(username="testUser")
        user.save()
        feature = Feature(title="Test Title",description="Test Description",status="progressed",author=user)
        feature.save()
        comment = CommentForFeature(comment="Test Comment", feature=feature, author=user)
        comment.save()
        self.assertEqual(comment.comment, "Test Comment")