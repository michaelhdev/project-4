from django.test import TestCase
from features.models import Feature
from django.contrib.auth.models import User

"""View tests for the cart app"""

class TestCartViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testUser30', password='testPassword')
        self.client.login(username='testUser30', password='testPassword')
    
    def test_view_cart(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
