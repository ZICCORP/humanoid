from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Profile

class TestSignal(TestCase):

    def test_create_profile(self):
        
        user = User.objects.create_user('user1','testpass123')
        
     
        p1 = Profile.objects.get(id=2)
       

        self.assertEqual(user.username,p1.user.username)

