from django.test import TestCase
from .models import Feature, CommentForFeature
from django.contrib import auth
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_features(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    def test_get_feature_details(self):
        user = User(username="testUser")
        user.save()
        feature = Feature(title="Test Title",description="Test Description",status="progressed",author=user)
        feature.save()

        page = self.client.get("/features/{0}/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureDetail.html")
        
    def test_get_details_of_but_that_does_not_exist(self):
        page = self.client.get("/features/2/")
        self.assertEqual(page.status_code, 404)
        
    def test_new_feature(self):
        page = self.client.get("/features/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureForm.html")
        
    def test_edit_feature(self):
        user = User(username="testUser")
        user.save()
        feature = Feature(title="Test Title",description="Test Description",status="progressed",author=user)
        feature.save()

        page = self.client.get("/features/{0}/edit/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureForm.html")
        
    def test_edit_feature_that_does_not_exist(self):
        page = self.client.get("/features/5/edit/")
        self.assertEqual(page.status_code, 404)
        
    
    