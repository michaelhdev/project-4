from django.test import TestCase
from django.contrib.auth.models import User

"""View tests for the checkout app"""

class TestCheckoutViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testUser30', password='testPassword')
        self.client.login(username='testUser30', password='testPassword')
        
    def test_checkout_page(self):
        
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
