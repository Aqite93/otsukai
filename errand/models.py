from django.db import models
from accounts.models import User
from otsukai.models import Category


class Errand(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024,
                                   blank=True,
                                   help_text='依頼内容を記載してください．')

    class Meta:
        db_table = 'errand'
