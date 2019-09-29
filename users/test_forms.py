from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

"""Form tests for the users app"""

class TestUserLoginForm(TestCase):
    
    def test_can_login_with_just_username(self):
        form = UserLoginForm({'username': 'Test user'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
        
    def test_can_login_with_just_password(self):
        form = UserLoginForm({'password': 'Test password'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_login_with_valid_info(self):
        form = UserLoginForm({'username': 'Test user','password': 'Test password'})
        self.assertTrue(form.is_valid())
        
class TestUserRegistrationForm(TestCase):
    
    def test_registration_valid_input(self):
        form = UserRegistrationForm({'username':'testUser','email':'testUser@gmail.com','password1':'testpassword','password2':'testpassword'})
        self.assertTrue(form.is_valid())
    
    def test_registration_invalid_email(self):
        form = UserRegistrationForm({'username':'testUser','email':'testUsergmail.com','password1':'testpassword','password2':'testpassword'})
        self.assertFalse(form.is_valid())
        
    def test_registration_different_passwords(self):
        form = UserRegistrationForm({'username':'testUser','email':'testUsergmail.com','password1':'testpassword','password2':'testpassword2'})
        self.assertFalse(form.is_valid())
        
    def test_registration_no_username(self):
        form = UserRegistrationForm({'username':'','email':'testUsergmail.com','password1':'testpassword','password2':'testpassword2'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
    
