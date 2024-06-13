from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser(account='2022152414', email='2022152414@example.com', password='wu12131415')