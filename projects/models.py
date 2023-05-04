from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Project(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    source_code = models.URLField(null=True, blank=True)
    deployed_url = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# Class for making comments
class Comment(models.Model):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"