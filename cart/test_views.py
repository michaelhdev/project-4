from django.test import TestCase
from features.models import Feature
from django.contrib.auth.models import User

class TestCartViews(TestCase):
    
    def test_view_cart(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
