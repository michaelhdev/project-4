from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

class TestMakePaymentForm(TestCase):
    
    def test_payment_form_valid_input(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "111",
                    'expiry_month': 4,
                    'expiry_year': 2025,
                    'stripe_id': 'Test'
        })
        self.assertTrue(form.is_valid())
        
     
    def test_payment_form_invalid_date(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "111",
                    'expiry_month': 4,
                    'expiry_year': 2010,
                    'stripe_id': 'Test'
        })
        self.assertFalse(form.is_valid())
        
class TestOrderForm(TestCase):
    
    def test_order_form_valid_input(self):
        form = OrderForm({
                    'full_name': "testName", 
                    'phone_number': "testPhoneNumber", 
                    'country': "testCountry",
                    'postcode': "testPostCode",
                    'town_or_city': "testTownCity",
                    'street_address1': "testStreet1",
                    'street_address2': "testStreet2",
                    'county': 'testCountry'
                    
        })
        self.assertTrue(form.is_valid())
    
    def test_order_form_no_name(self):
        form = OrderForm({
                    'full_name': "", 
                    'phone_number': "testPhoneNumber", 
                    'country': "testCountry",
                    'postcode': "testPostCode",
                    'town_or_city': "testTownCity",
                    'street_address1': "testStreet1",
                    'street_address2': "testStreet2",
                    'county': 'testCountry'
                    
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])