from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),

    (1,"Publish")
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    img = models.ImageField(upload_to='profile-images',blank=True)


    def __str__(self):
        return self.user.username


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')

    title = models.CharField(max_length=200)
    
    slug = models.SlugField(max_length=200, unique=True)

    cover = models.ImageField(upload_to='cover-images')

    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class CommentManager(models.Manager):

    def active(self):

        return self.filter(active=True)


class Comment(models.Model):
    objects = CommentManager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

    name = models.CharField(max_length=80)

    email = models.EmailField()

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    class Meta:
        
        ordering = ['-created_on']

    def __str__(self):

        return 'Comment {} by {}'.format(self.post.title , self.name)