from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


class Profile(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    followers = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create Profile When New User Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile.objects.create(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
