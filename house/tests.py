from django.test import TestCase
from .models import *

# Create your tests here.

class testModels:
    def setUp(self):
        self.user = User.objects.create(id=1, username='ben')
        self.post = Post.objects.create(id=1, title='test post', photo='img.jpg', description='desc',
                                        user=self.user, page='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)