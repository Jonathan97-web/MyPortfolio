from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    intro = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
