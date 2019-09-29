from django.test import TestCase

"""View tests for the users app"""

class TestUserViews(TestCase):
      
    def test_get_login(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_get_register(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    
        