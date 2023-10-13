from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Profile(models.Model):
    """
    User profile model.
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the profile.
        """
        return self.user.email