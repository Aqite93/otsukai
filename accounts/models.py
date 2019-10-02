from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
GENDER_CHOICES = [
    ('man', '男性'),
    ('woman', '女性')
]


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('User Name', max_length=100)
    password = models.CharField('Password', max_length=100)
    address = models.CharField('Address', max_length=1024)
    age = models.CharField('Age', max_length=256)
    gender = models.CharField('gender', max_length=10, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
