from django.test import TestCase
from .models import Bug, CommentForBug
from django.contrib import auth
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_bugs(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
    def test_get_bug_details(self):
        user = User(username="testUser")
        user.save()
        bug = Bug(title="Test Title",description="Test Description",status="progressed",author=user)
        bug.save()

        page = self.client.get("/bugs/{0}/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugDetail.html")
        
    def test_get_details_of_but_that_does_not_exist(self):
        page = self.client.get("/bugs/2/")
        self.assertEqual(page.status_code, 404)
        
    def test_new_bug(self):
        page = self.client.get("/bugs/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugForm.html")
        
    def test_edit_bug(self):
        user = User(username="testUser")
        user.save()
        bug = Bug(title="Test Title",description="Test Description",status="progressed",author=user)
        bug.save()

        page = self.client.get("/bugs/{0}/edit/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugForm.html")
        
    def test_edit_bug_that_does_not_exist(self):
        page = self.client.get("/bugs/5/edit/")
        self.assertEqual(page.status_code, 404)
        
    
    