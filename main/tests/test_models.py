from django.test import TestCase
from main.models import Post
from django.contrib.auth.models import User

class TestModel(TestCase):

    def test_post(self):

        user1 = User.objects.create_user(
            "user1", "testpass123"
        )

        p1=Post.objects.create(author=user1,title='frank',content='Hello world')

        self.assertEqual(p1.title,'frank')

        self.assertEqual(p1.content,'Hello world')

