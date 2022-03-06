from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserTest(TestCase):
    User = get_user_model()
    def setUp(self):
        User.objects.create(username="test", email="test@test.test", password="test")  
        User.objects.create(username="admin", email="admin@admin.admin", \
                password='admin', is_staff=True, is_superuser=True)

    def test_get_models(self):
        test = User.objects.get(username='test')
        admin = User.objects.get(username='admin')
        self.assertEqual(
            test.email, "test@test.test"
        )
        self.assertEqual(
            admin.email, 'admin@admin.admin'
        )