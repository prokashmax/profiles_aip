from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manger User Profile """
    def create_user(self, email, name, password=None):
        """Create  for user profile """
        if not email:
            raise ValueError('User Must Have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_supperuser(self, email, name, password):
        """create and save New  supperuser give with details"""
        user = self.create_user(email, name, password)

        user.is_supperuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database Models for users in the system """
    email = models.EmailField(max_length=225,unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name

    def __str__(self):
        """ return repragentaion of user email id"""
        return self.name
