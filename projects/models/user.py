from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=100)
    password = models.CharField(_('password'), max_length=100)
    address = models.CharField(_('address'), max_length=1024)
    age = models.CharField(_('age'), max_length=256)
    gender = models.CharField(_('gender'))

    class Meta:
        db_table = 'user'

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
