from django.test import TestCase
from .models import Bug, CommentForBug
from django.contrib.auth.models import User

"""
    Tests for bug models
"""

class TestBugModel(TestCase):

    def test_bug_creation(self):
        user = User(username="testUser")
        user.save()
        bug = Bug(title="Test Title",description="Test Description",status="progressed",author=user)
        bug.save()
        self.assertEqual(bug.title, "Test Title")
        
class TestCommentModel(TestCase):

    def test_comment_creation(self):
        user = User(username="testUser")
        user.save()
        bug = Bug(title="Test Title",description="Test Description",status="progressed",author=user)
        bug.save()
        comment = CommentForBug(comment="Test Comment", bug=bug, author=user)
        comment.save()
        self.assertEqual(comment.comment, "Test Comment")