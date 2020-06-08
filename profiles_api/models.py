from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Overriding Django default User Model

class UserProfileManager(BaseUserManager):
    """ Manager for User Profiles such as creating a new user and creating superuser form command line since we are overriding the
    default user so we need a manager class which will handle the overridden user fields"""

    def create_user(self, email, name, password=None):
        """ Creates a new Profile """
        if not email:
            raise ValueError('You must provide email address')

        email = self.normalize_email(email)  # defined in BaseUserManager used for making email lowercase
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, name, password):
        """ Creates and saves a new Superuser with given details """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ DATABASE MODEL FOR USER IN DJANGO APP """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Overriding the object field ro handle user creation logic in UserProfileManager class
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # overriding default username as email. Earlier it was username
    REQUIRED_FIELDS = ['name']  # making name as required field

    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    def __str__(self):
        """ Returns String Representation of our user"""
        return self.email
