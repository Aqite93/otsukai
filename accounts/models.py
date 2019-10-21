from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.
GENDER_CHOICES = [
    ('man', '男性'),
    ('woman', '女性')
]


class UserExtendManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('User Name', max_length=100)
    password = models.CharField('Password', max_length=100)
    address = models.CharField('Address', max_length=1024)
    age = models.CharField('Age', max_length=256)
    gender = models.CharField('gender', max_length=10, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'

    objects = UserExtendManager()

    class Meta:
        db_table = 'user'
