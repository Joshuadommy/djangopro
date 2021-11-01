from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='josh',
            email='josh@djangopro.com',
            password='tudom/2017'
        )
        self.assertEqual(user.username, 'josh')
        self.assertEqual(user.email, 'josh@djangopro.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_user(
            username='josh',
            email='josh@djangopro.com',
            password='tudom/2017'
        )
        self.assertEqual(admin_user.username, 'josh')
        self.assertEqual(admin_user.email, 'josh@djangopro.com')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)
