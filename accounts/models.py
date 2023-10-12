# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model extending AbstractBaseUser and PermissionsMixin.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """
        Returns a string representation of the user.
        """
        return self.email
    
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
    
class Address(models.Model):
    """
    User address model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"